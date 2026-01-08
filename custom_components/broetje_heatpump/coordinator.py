"""DataUpdateCoordinator for the Brötje Heatpump integration."""

from __future__ import annotations

import asyncio
import logging
from datetime import timedelta
from typing import Any

from pymodbus.client import AsyncModbusTcpClient
from pymodbus.exceptions import ModbusException

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, CONF_PORT, Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import (
    BINARY_SENSORS,
    CONF_UNIT_ID,
    DEFAULT_MODEL,
    DEFAULT_SCAN_INTERVAL,
    DEFAULT_UNIT_ID,
    DOMAIN,
    MANUFACTURER,
    REG_HOLDING,
    REG_INPUT,
    REGISTER_MAP,
    SENSORS,
)

_LOGGER = logging.getLogger(__name__)


class BroetjeModbusCoordinator(DataUpdateCoordinator[dict[str, Any]]):
    """Coordinator for fetching data from Brötje Heatpump via Modbus."""

    config_entry: ConfigEntry

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """Initialize the coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            config_entry=entry,
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )
        self._host = entry.data[CONF_HOST]
        self._port = entry.data[CONF_PORT]
        self._unit_id = entry.data.get(CONF_UNIT_ID, DEFAULT_UNIT_ID)
        self._client: AsyncModbusTcpClient | None = None
        self._lock = asyncio.Lock()

        # Device info
        self.device_serial: str | None = None
        self.device_model: str = DEFAULT_MODEL
        self.device_manufacturer: str = MANUFACTURER
        self.device_firmware: str | None = None

    async def _async_setup(self) -> None:
        """Set up the coordinator (called during first refresh)."""
        await self._connect()
        await self._read_device_info()

    async def _connect(self) -> None:
        """Establish connection to the Modbus device."""
        if self._client is not None and self._client.connected:
            return

        self._client = AsyncModbusTcpClient(
            host=self._host,
            port=self._port,
        )

        if not await self._client.connect():
            raise UpdateFailed(f"Failed to connect to {self._host}:{self._port}")

        _LOGGER.debug("Connected to Modbus device at %s:%s", self._host, self._port)

    async def _disconnect(self) -> None:
        """Disconnect from the Modbus device."""
        if self._client is not None:
            self._client.close()
            self._client = None
            _LOGGER.debug("Disconnected from Modbus device")

    async def _read_device_info(self) -> None:
        """Read device identification information."""
        # TODO: Implement reading device info from Modbus registers
        # This will be populated once we have the register addresses from the PDF
        pass

    async def _read_registers(
        self,
        address: int,
        count: int,
        register_type: str,
    ) -> list[int] | None:
        """Read registers from the Modbus device."""
        async with self._lock:
            try:
                await self._connect()

                if register_type == REG_INPUT:
                    result = await self._client.read_input_registers(
                        address=address, count=count, device_id=self._unit_id
                    )
                elif register_type == REG_HOLDING:
                    result = await self._client.read_holding_registers(
                        address=address, count=count, device_id=self._unit_id
                    )
                else:
                    _LOGGER.error("Unknown register type: %s", register_type)
                    return None

                if result.isError():
                    _LOGGER.warning(
                        "Modbus error reading address %s: %s",
                        address,
                        result,
                    )
                    return None

                return list(result.registers)

            except ModbusException as err:
                _LOGGER.error("Modbus exception: %s", err)
                await self._disconnect()
                return None

    def _get_needed_registers(self) -> set[str]:
        """Get the set of register keys needed by enabled entities.

        This checks the entity registry to determine which entities are enabled.
        If an entity is not yet in the registry (first refresh), it's assumed needed.
        Only entities explicitly disabled by the user are skipped.
        """
        entity_registry = er.async_get(self.hass)
        device_id = self.config_entry.unique_id or self.config_entry.entry_id

        needed_registers: set[str] = set()

        # Check sensors
        for sensor_key, sensor_config in SENSORS.items():
            unique_id = f"{device_id}_{sensor_key}"
            entity_id = entity_registry.async_get_entity_id(
                Platform.SENSOR, DOMAIN, unique_id
            )

            # If entity doesn't exist in registry yet, assume we need it
            if entity_id is None:
                needed_registers.add(sensor_config["register"])
                continue

            entry = entity_registry.async_get(entity_id)
            # If entity exists and is NOT disabled, we need this register
            if entry and not entry.disabled:
                needed_registers.add(sensor_config["register"])

        # Check binary sensors
        for sensor_key, sensor_config in BINARY_SENSORS.items():
            unique_id = f"{device_id}_{sensor_key}"
            entity_id = entity_registry.async_get_entity_id(
                Platform.BINARY_SENSOR, DOMAIN, unique_id
            )

            # If entity doesn't exist in registry yet, assume we need it
            if entity_id is None:
                needed_registers.add(sensor_config["register"])
                continue

            entry = entity_registry.async_get(entity_id)
            # If entity exists and is NOT disabled, we need this register
            if entry and not entry.disabled:
                needed_registers.add(sensor_config["register"])

        return needed_registers

    def _group_registers_for_batch_read(
        self, register_keys: set[str]
    ) -> list[dict[str, Any]]:
        """Group registers into batches for efficient reading.

        Groups consecutive or near-consecutive registers to minimize
        the number of Modbus read operations. Reading a few unused
        registers between needed ones is much cheaper than making
        separate Modbus requests.
        """
        if not register_keys:
            return []

        # Modbus limits: max 125 registers per read, we use 100 for safety
        MAX_BATCH_SIZE = 100
        # Max gap between registers to still batch them together
        # Reading unused registers is cheap; extra round-trips are expensive
        MAX_GAP = 50

        # Build list of register info and sort by type, then address
        registers: list[dict[str, Any]] = []
        for key in register_keys:
            config = REGISTER_MAP[key]
            registers.append({
                "key": key,
                "address": config["address"],
                "count": config.get("count", 1),
                "type": config["type"],
                "config": config,
            })

        # Sort by register type first (to group holding/input), then by address
        registers.sort(key=lambda x: (x["type"], x["address"]))

        # Group into batches
        batches: list[dict[str, Any]] = []
        current_batch: dict[str, Any] | None = None

        for reg in registers:
            reg_end = reg["address"] + reg["count"] - 1

            if current_batch is None:
                # Start new batch
                current_batch = {
                    "type": reg["type"],
                    "start_address": reg["address"],
                    "end_address": reg_end,
                    "registers": [reg],
                }
            elif (
                reg["type"] == current_batch["type"]
                and reg["address"] <= current_batch["end_address"] + MAX_GAP + 1
                and (reg_end - current_batch["start_address"] + 1) <= MAX_BATCH_SIZE
            ):
                # Add to current batch
                current_batch["registers"].append(reg)
                current_batch["end_address"] = max(current_batch["end_address"], reg_end)
            else:
                # Finish current batch and start new one
                batches.append(current_batch)
                current_batch = {
                    "type": reg["type"],
                    "start_address": reg["address"],
                    "end_address": reg_end,
                    "registers": [reg],
                }

        if current_batch:
            batches.append(current_batch)

        return batches

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch data from the Modbus device."""
        data: dict[str, Any] = {}

        # Get only the registers needed by enabled entities
        needed_registers = self._get_needed_registers()

        if not needed_registers:
            _LOGGER.debug("No enabled entities, skipping Modbus read")
            return data

        # Group registers into batches for efficient reading
        batches = self._group_registers_for_batch_read(needed_registers)

        _LOGGER.debug(
            "Reading %d registers in %d batch(es) for enabled entities",
            len(needed_registers),
            len(batches),
        )

        try:
            async with asyncio.timeout(30):
                for batch in batches:
                    start_addr = batch["start_address"]
                    count = batch["end_address"] - start_addr + 1

                    _LOGGER.debug(
                        "Batch read: type=%s, address=%d, count=%d (%d registers)",
                        batch["type"],
                        start_addr,
                        count,
                        len(batch["registers"]),
                    )

                    result = await self._read_registers(
                        start_addr, count, batch["type"]
                    )

                    if result is not None:
                        # Extract individual register values from batch response
                        for reg in batch["registers"]:
                            offset = reg["address"] - start_addr
                            reg_count = reg["count"]
                            reg_values = result[offset : offset + reg_count]

                            if len(reg_values) == reg_count:
                                data[reg["key"]] = self._process_register_value(
                                    reg_values, reg["config"]
                                )
                            else:
                                _LOGGER.warning(
                                    "Incomplete data for register %s at address %d",
                                    reg["key"],
                                    reg["address"],
                                )
                                data[reg["key"]] = None
                    else:
                        # Batch read failed, mark all registers in batch as None
                        for reg in batch["registers"]:
                            data[reg["key"]] = None

        except TimeoutError as err:
            raise UpdateFailed("Timeout communicating with device") from err
        except ModbusException as err:
            raise UpdateFailed(f"Modbus error: {err}") from err

        return data

    def _process_register_value(
        self,
        registers: list[int],
        config: dict[str, Any],
    ) -> Any:
        """Process raw register values based on configuration."""
        data_type = config.get("data_type", "int16")
        scale = config.get("scale", 1.0)
        bit = config.get("bit")

        if data_type == "bool":
            value = registers[0]
            if bit is not None:
                return bool(value & (1 << bit))
            return bool(value)

        if data_type == "int16":
            value = registers[0]
            # Convert to signed if necessary
            if value >= 32768:
                value -= 65536
            return value * scale

        if data_type == "uint16":
            return registers[0] * scale

        if data_type == "int32":
            value = (registers[0] << 16) | registers[1]
            if value >= 2147483648:
                value -= 4294967296
            return value * scale

        if data_type == "uint32":
            value = (registers[0] << 16) | registers[1]
            return value * scale

        if data_type == "string":
            # Decode registers as ASCII string
            chars = []
            for reg in registers:
                chars.append(chr((reg >> 8) & 0xFF))
                chars.append(chr(reg & 0xFF))
            return "".join(chars).rstrip("\x00").strip()

        return registers[0] * scale

    async def async_shutdown(self) -> None:
        """Shutdown the coordinator."""
        await self._disconnect()
        await super().async_shutdown()
