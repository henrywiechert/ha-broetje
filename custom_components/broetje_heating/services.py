"""Services: zone boost and debug raw Modbus register access.

``zone_boost`` writes the zone "End change mode time" timestamp register.

DANGER: The debug services bypass the register_map entirely. They read and
write raw register words directly by address, with no knowledge of what
a register actually means, no bounds checking, and no scaling. They are
intended for diagnosing undocumented registers and are only usable for
config entries that have explicitly enabled "Debug register access" in
the integration options.
"""

from __future__ import annotations

from datetime import timedelta
from typing import Any

import voluptuous as vol
from homeassistant.config_entries import ConfigEntry, ConfigEntryState
from homeassistant.core import HomeAssistant, ServiceCall, SupportsResponse, callback
from homeassistant.exceptions import ServiceValidationError
from homeassistant.helpers import config_validation as cv
from homeassistant.util import dt as dt_util

from .const import (
    ATTR_ADDRESS,
    ATTR_CONFIG_ENTRY_ID,
    ATTR_CONFIRM,
    ATTR_CONTROL_MODE,
    ATTR_COUNT,
    ATTR_DATA_TYPE,
    ATTR_DURATION,
    ATTR_REGISTER_TYPE,
    ATTR_VALUES,
    ATTR_ZONE,
    CONF_DEBUG_REGISTER_ACCESS,
    DOMAIN,
    REG_HOLDING,
    REG_INPUT,
    SERVICE_READ_REGISTER,
    SERVICE_WRITE_REGISTER,
    SERVICE_ZONE_BOOST,
)
from .coordinator import BroetjeModbusCoordinator
from .timestamp import decode_time_of_day

MAX_MODBUS_REGISTERS = 125

SERVICE_READ_REGISTER_SCHEMA = vol.Schema(
    {
        vol.Required(ATTR_CONFIG_ENTRY_ID): cv.string,
        vol.Required(ATTR_ADDRESS): vol.All(int, vol.Range(min=0, max=65535)),
        vol.Optional(ATTR_COUNT, default=1): vol.All(
            int, vol.Range(min=1, max=MAX_MODBUS_REGISTERS)
        ),
        vol.Optional(ATTR_REGISTER_TYPE, default=REG_HOLDING): vol.In(
            [REG_HOLDING, REG_INPUT]
        ),
        vol.Optional(ATTR_DATA_TYPE, default="raw"): vol.In(
            ["raw", "uint16", "int16", "uint32", "int32", "string", "time_of_day"]
        ),
    }
)

CONTROL_MODE_KEEP = "keep"
CONTROL_MODE_MANUAL = "manual"

SERVICE_ZONE_BOOST_SCHEMA = vol.Schema(
    {
        vol.Required(ATTR_CONFIG_ENTRY_ID): cv.string,
        vol.Required(ATTR_ZONE): vol.All(int, vol.Range(min=1, max=12)),
        vol.Optional(ATTR_DURATION, default=30): vol.All(
            int, vol.Range(min=1, max=1440)
        ),
        vol.Optional(ATTR_CONTROL_MODE, default=CONTROL_MODE_KEEP): vol.In(
            [CONTROL_MODE_KEEP, CONTROL_MODE_MANUAL]
        ),
    }
)

SERVICE_WRITE_REGISTER_SCHEMA = vol.Schema(
    {
        vol.Required(ATTR_CONFIG_ENTRY_ID): cv.string,
        vol.Required(ATTR_ADDRESS): vol.All(int, vol.Range(min=0, max=65535)),
        vol.Required(ATTR_VALUES): vol.All(
            cv.ensure_list,
            [vol.All(int, vol.Range(min=0, max=65535))],
            vol.Length(min=1, max=MAX_MODBUS_REGISTERS),
        ),
        vol.Required(ATTR_CONFIRM): vol.Equal(
            True,
            msg="You must set confirm: true to acknowledge the risk of a raw write",
        ),
    }
)


def _format_timestamp(value: Any) -> str | None:
    return value.isoformat() if value is not None else None


def _decode_registers(registers: list[int], data_type: str) -> Any:
    """Decode raw register words for display purposes only."""
    if data_type == "raw":
        return registers
    if data_type == "uint16":
        return registers[0]
    if data_type == "int16":
        value = registers[0]
        return value - 65536 if value >= 32768 else value
    if data_type in ("uint32", "int32"):
        if len(registers) < 2:
            raise ServiceValidationError(
                f"data_type '{data_type}' requires count=2, got {len(registers)}"
            )
        value = (registers[0] << 16) | registers[1]
        if data_type == "int32" and value >= 2147483648:
            value -= 4294967296
        return value
    if data_type == "time_of_day":
        # Byte order of the 6-byte timestamp is unverified: show both
        return {
            "big_endian": _format_timestamp(decode_time_of_day(registers, "big")),
            "little_endian": _format_timestamp(decode_time_of_day(registers, "little")),
        }
    if data_type == "string":
        chars = [chr((reg >> 8) & 0xFF) + chr(reg & 0xFF) for reg in registers]
        return "".join(chars).rstrip("\x00").strip()
    return registers


def _get_coordinator(
    hass: HomeAssistant, config_entry_id: str
) -> tuple[ConfigEntry, BroetjeModbusCoordinator]:
    """Resolve the coordinator of a loaded Brötje config entry."""
    entry = hass.config_entries.async_get_entry(config_entry_id)
    if entry is None or entry.domain != DOMAIN:
        raise ServiceValidationError(
            f"'{config_entry_id}' is not a Brötje Heating config entry"
        )
    if entry.state is not ConfigEntryState.LOADED:
        raise ServiceValidationError(f"Config entry '{entry.title}' is not loaded")
    return entry, entry.runtime_data


def _get_debug_coordinator(
    hass: HomeAssistant, config_entry_id: str
) -> BroetjeModbusCoordinator:
    """Resolve and authorize the coordinator for a debug service call."""
    entry, coordinator = _get_coordinator(hass, config_entry_id)
    if not entry.options.get(CONF_DEBUG_REGISTER_ACCESS, False):
        raise ServiceValidationError(
            f"Debug register access is disabled for '{entry.title}'. Enable "
            "'Debug register access (DANGER)' in the integration options "
            "before using this action."
        )
    return coordinator


@callback
def async_setup_services(hass: HomeAssistant) -> None:
    """Register the debug register read/write services (once per HA instance)."""
    if hass.services.has_service(DOMAIN, SERVICE_READ_REGISTER):
        return

    async def _async_read_register(call: ServiceCall) -> dict[str, Any]:
        coordinator = _get_debug_coordinator(hass, call.data[ATTR_CONFIG_ENTRY_ID])
        address = call.data[ATTR_ADDRESS]
        count = call.data[ATTR_COUNT]
        register_type = call.data[ATTR_REGISTER_TYPE]
        data_type = call.data[ATTR_DATA_TYPE]

        registers = await coordinator.async_debug_read_registers(
            address, count, register_type
        )

        return {
            "address": address,
            "count": count,
            "register_type": register_type,
            "data_type": data_type,
            "raw_registers": registers,
            "hex": [f"0x{value:04X}" for value in registers],
            "decoded": _decode_registers(registers, data_type),
        }

    async def _async_write_register(call: ServiceCall) -> dict[str, Any]:
        coordinator = _get_debug_coordinator(hass, call.data[ATTR_CONFIG_ENTRY_ID])
        address = call.data[ATTR_ADDRESS]
        values = call.data[ATTR_VALUES]

        readback = await coordinator.async_debug_write_registers(address, values)

        return {
            "address": address,
            "values_written": values,
            "readback": readback,
        }

    async def _async_zone_boost(call: ServiceCall) -> dict[str, Any]:
        _, coordinator = _get_coordinator(hass, call.data[ATTR_CONFIG_ENTRY_ID])
        zone = call.data[ATTR_ZONE]
        duration = call.data[ATTR_DURATION]
        end_key = f"zone{zone}_end_change_mode_time"
        mode_key = f"zone{zone}_control_mode"

        if end_key not in coordinator.register_map:
            raise ServiceValidationError(
                f"Zone {zone} is not configured (or this device does not "
                "support the zone boost)"
            )

        # The device has no timezone: send HA local wall-clock time.
        end = (dt_util.now() + timedelta(minutes=duration)).replace(
            tzinfo=None, microsecond=0
        )
        words, readback = await coordinator.async_write_time_of_day(end_key, end)

        if call.data[ATTR_CONTROL_MODE] == CONTROL_MODE_MANUAL:
            await coordinator.async_write_register(mode_key, 1)

        return {
            "zone": zone,
            "end_time": end.isoformat(),
            "raw_registers": words,
            "readback_end_time": _format_timestamp(readback),
            "control_mode": call.data[ATTR_CONTROL_MODE],
        }

    hass.services.async_register(
        DOMAIN,
        SERVICE_ZONE_BOOST,
        _async_zone_boost,
        schema=SERVICE_ZONE_BOOST_SCHEMA,
        supports_response=SupportsResponse.OPTIONAL,
    )
    hass.services.async_register(
        DOMAIN,
        SERVICE_READ_REGISTER,
        _async_read_register,
        schema=SERVICE_READ_REGISTER_SCHEMA,
        supports_response=SupportsResponse.ONLY,
    )
    hass.services.async_register(
        DOMAIN,
        SERVICE_WRITE_REGISTER,
        _async_write_register,
        schema=SERVICE_WRITE_REGISTER_SCHEMA,
        supports_response=SupportsResponse.ONLY,
    )
