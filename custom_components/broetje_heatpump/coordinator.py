"""DataUpdateCoordinator for the Brötje Heatpump integration."""

from __future__ import annotations

import asyncio
import logging
from datetime import timedelta
from typing import Any

from pymodbus.client import AsyncModbusTcpClient
from pymodbus.exceptions import ModbusException

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_HOST, CONF_PORT
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import (
    CONF_UNIT_ID,
    DEFAULT_MODEL,
    DEFAULT_SCAN_INTERVAL,
    DEFAULT_UNIT_ID,
    DOMAIN,
    MANUFACTURER,
    REG_HOLDING,
    REG_INPUT,
    REGISTER_MAP,
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

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch data from the Modbus device."""
        data: dict[str, Any] = {}

        try:
            async with asyncio.timeout(10):
                for key, reg_config in REGISTER_MAP.items():
                    result = await self._read_registers(
                        reg_config["address"],
                        reg_config.get("count", 1),
                        reg_config["type"],
                    )

                    if result is not None:
                        data[key] = self._process_register_value(result, reg_config)
                    else:
                        data[key] = None

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
