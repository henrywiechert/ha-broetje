"""Config flow for Brötje Heatpump integration."""

from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant.config_entries import (
    ConfigEntry,
    ConfigFlow,
    ConfigFlowResult,
    OptionsFlow,
)
from homeassistant.const import CONF_HOST, CONF_PORT
from homeassistant.helpers.selector import (
    SelectOptionDict,
    SelectSelector,
    SelectSelectorConfig,
    SelectSelectorMode,
)

from .const import (
    CONF_SCAN_INTERVAL,
    CONF_UNIT_ID,
    DEFAULT_PORT,
    DEFAULT_SCAN_INTERVAL,
    DEFAULT_UNIT_ID,
    DOMAIN,
)
from .devices import CONF_DEVICE_TYPE, DEVICE_MODELS, DeviceType
from .devices.iwr import ZONE_ADDR_OFFSET, ZONE_FUNCTION_BASE_ADDR, ZONE_TYPE_BASE_ADDR

_LOGGER = logging.getLogger(__name__)

STEP_CONNECTION_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_HOST): str,
        vol.Required(CONF_PORT, default=DEFAULT_PORT): int,
        vol.Required(CONF_UNIT_ID, default=DEFAULT_UNIT_ID): int,
    }
)

_ZONE_TYPE_LABELS: dict[int, str] = {
    0: "not present",
    1: "CH only",
    2: "CH + cooling",
    3: "DHW",
    4: "process heat",
    5: "swimming pool",
    254: "other",
}

_ZONE_FUNCTION_LABELS: dict[int, str] = {
    0: "disable",
    1: "direct",
    2: "mixing circuit",
    3: "swimming pool",
    4: "high temperature",
    5: "fan convector",
    6: "DHW tank",
    7: "electrical DHW",
    8: "time program",
    9: "process heat",
    10: "DHW layered",
    11: "DHW internal tank",
    12: "DHW commercial tank",
    13: "occupied",
    254: "DHW primary",
}


class CannotConnect(Exception):
    """Error to indicate we cannot connect."""


async def detect_zones(client: Any, unit_id: int) -> list[dict[str, Any]]:
    """Read zone_type and zone_function registers for all 12 zones.

    Returns list of 12 dicts with keys: zone, zone_type, zone_function, active, label.
    """
    _LOGGER.debug(
        "Starting zone detection for unit_id=%d, client connected=%s",
        unit_id,
        getattr(client, "connected", "unknown"),
    )
    results: list[dict[str, Any]] = []
    for z in range(12):
        zn = z + 1
        type_addr = ZONE_TYPE_BASE_ADDR + ZONE_ADDR_OFFSET * z
        func_addr = ZONE_FUNCTION_BASE_ADDR + ZONE_ADDR_OFFSET * z

        zone_type = 0
        zone_function = 0

        try:
            type_result = await client.read_holding_registers(
                address=type_addr, count=1, device_id=unit_id
            )
            if type_result.isError():
                _LOGGER.warning(
                    "Zone %d: zone_type read error at addr %d: %s",
                    zn,
                    type_addr,
                    type_result,
                )
            else:
                zone_type = type_result.registers[0]

            func_result = await client.read_holding_registers(
                address=func_addr, count=1, device_id=unit_id
            )
            if func_result.isError():
                _LOGGER.warning(
                    "Zone %d: zone_function read error at addr %d: %s",
                    zn,
                    func_addr,
                    func_result,
                )
            else:
                zone_function = func_result.registers[0]
        except Exception:
            _LOGGER.exception("Zone %d: exception reading registers", zn)

        _LOGGER.debug("Zone %d: type=%d, function=%d", zn, zone_type, zone_function)
        active = zone_type != 0
        type_label = _ZONE_TYPE_LABELS.get(zone_type, f"type {zone_type}")
        func_label = _ZONE_FUNCTION_LABELS.get(zone_function, f"func {zone_function}")

        if zone_type == 0:
            label = f"Zone {zn} — not present"
        else:
            label = f"Zone {zn} — {type_label}, {func_label}"

        results.append(
            {
                "zone": zn,
                "zone_type": zone_type,
                "zone_function": zone_function,
                "active": active,
                "label": label,
            }
        )

    return results


def _build_zone_select_schema(
    zone_options: list[SelectOptionDict],
    preselected: list[str],
) -> vol.Schema:
    """Build a voluptuous schema with a multi-select zone selector."""
    return vol.Schema(
        {
            vol.Required("zones", default=preselected): SelectSelector(
                SelectSelectorConfig(
                    options=zone_options,
                    multiple=True,
                    mode=SelectSelectorMode.LIST,
                )
            )
        }
    )


def _parse_zone_selection(user_input: dict[str, Any]) -> list[int]:
    """Parse zone selection from form input, returning sorted 1-based zone numbers."""
    return sorted(int(z) for z in user_input["zones"])


# ---------------------------------------------------------------------------
# Options flow
# ---------------------------------------------------------------------------


class BroetjeOptionsFlow(OptionsFlow):
    """Handle options for Brötje Heatpump."""

    def __init__(self) -> None:
        """Initialize options flow."""
        self._zone_options: list[SelectOptionDict] = []
        self._preselected: list[str] = []

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Entry point: show menu for IWR, or go straight to general for ISR."""
        device_type = self.config_entry.data.get(CONF_DEVICE_TYPE)
        if device_type == DeviceType.IWR.value:
            return self.async_show_menu(
                step_id="init",
                menu_options=["general", "zone_config"],
            )
        return await self.async_step_general(user_input)

    async def async_step_general(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Manage scan interval options."""
        if user_input is not None:
            return self.async_create_entry(data=user_input)

        current_interval = self.config_entry.options.get(
            CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL
        )

        return self.async_show_form(
            step_id="general",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_SCAN_INTERVAL, default=current_interval): vol.All(
                        int, vol.Range(min=10, max=3600)
                    ),
                }
            ),
        )

    async def async_step_zone_config(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Zone configuration sub-menu: autodetect or manual."""
        return self.async_show_menu(
            step_id="zone_config",
            menu_options=["zones_auto", "zones_manual"],
        )

    async def async_step_zones_auto(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Autodetect zones via the running coordinator."""
        if user_input is not None:
            return await self._async_save_zones(user_input)

        coordinator = self.config_entry.runtime_data
        zone_info = await detect_zones(coordinator._client, coordinator._unit_id)

        self._zone_options = [
            SelectOptionDict(value=str(z["zone"]), label=z["label"]) for z in zone_info
        ]
        self._preselected = [str(z["zone"]) for z in zone_info if z["active"]]

        return self.async_show_form(
            step_id="zones_auto",
            data_schema=_build_zone_select_schema(
                self._zone_options, self._preselected
            ),
        )

    async def async_step_zones_manual(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Manually select zones with current zones pre-checked."""
        if user_input is not None:
            return await self._async_save_zones(user_input)

        current_zones = self.config_entry.data.get("zones", [1])
        self._zone_options = [
            SelectOptionDict(value=str(z), label=f"Zone {z}") for z in range(1, 13)
        ]
        self._preselected = [str(z) for z in current_zones]

        return self.async_show_form(
            step_id="zones_manual",
            data_schema=_build_zone_select_schema(
                self._zone_options, self._preselected
            ),
        )

    async def _async_save_zones(self, user_input: dict[str, Any]) -> ConfigFlowResult:
        """Save the selected zones to entry.data and trigger reload."""
        zones = _parse_zone_selection(user_input)
        new_data = {**self.config_entry.data, "zones": zones}
        self.hass.config_entries.async_update_entry(self.config_entry, data=new_data)
        return self.async_create_entry(data=self.config_entry.options)


# ---------------------------------------------------------------------------
# Config flow
# ---------------------------------------------------------------------------


class BroetjeHeatpumpConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Brötje Heatpump."""

    VERSION = 3
    MINOR_VERSION = 1

    @staticmethod
    def async_get_options_flow(
        config_entry: ConfigEntry,
    ) -> BroetjeOptionsFlow:
        """Get the options flow handler."""
        return BroetjeOptionsFlow()

    def __init__(self) -> None:
        """Initialize the flow."""
        self._device_type: DeviceType | None = None
        self._connection_data: dict[str, Any] = {}
        self._zone_options: list[SelectOptionDict] = []
        self._preselected: list[str] = []

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle device type selection via menu."""
        return self.async_show_menu(
            step_id="user",
            menu_options=["isr", "iwr"],
        )

    async def async_step_isr(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle ISR connection setup."""
        self._device_type = DeviceType.ISR
        return await self._async_step_connection(user_input)

    async def async_step_iwr(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle IWR connection setup."""
        self._device_type = DeviceType.IWR
        return await self._async_step_connection(user_input)

    async def _async_step_connection(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle connection details (shared by ISR and IWR steps)."""
        errors: dict[str, str] = {}

        if user_input is not None:
            try:
                await self._test_connection(
                    user_input[CONF_HOST],
                    user_input[CONF_PORT],
                    user_input[CONF_UNIT_ID],
                )
            except CannotConnect:
                errors["base"] = "cannot_connect"
            except Exception:
                _LOGGER.exception("Unexpected exception")
                errors["base"] = "unknown"
            else:
                if self._device_type == DeviceType.IWR:
                    self._connection_data = user_input
                    return await self.async_step_iwr_zone_method()

                return await self._async_create_entry(user_input)

        return self.async_show_form(
            step_id=self._device_type.value,
            data_schema=STEP_CONNECTION_DATA_SCHEMA,
            errors=errors,
        )

    async def async_step_iwr_zone_method(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Zone configuration method menu: autodetect or manual."""
        return self.async_show_menu(
            step_id="iwr_zone_method",
            menu_options=["iwr_zones_auto", "iwr_zones_manual"],
        )

    async def async_step_iwr_zones_auto(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Autodetect zones and present multi-select with pre-checked active zones."""
        if user_input is not None:
            self._connection_data["zones"] = _parse_zone_selection(user_input)
            return await self._async_create_entry(self._connection_data)

        from pymodbus.client import AsyncModbusTcpClient

        client = AsyncModbusTcpClient(
            host=self._connection_data[CONF_HOST],
            port=self._connection_data[CONF_PORT],
        )
        try:
            connected = await client.connect()
            if not connected:
                _LOGGER.error("Zone detection: failed to connect to Modbus device")
            zone_info = await detect_zones(client, self._connection_data[CONF_UNIT_ID])
        finally:
            client.close()

        self._zone_options = [
            SelectOptionDict(value=str(z["zone"]), label=z["label"]) for z in zone_info
        ]
        self._preselected = [str(z["zone"]) for z in zone_info if z["active"]]

        return self.async_show_form(
            step_id="iwr_zones_auto",
            data_schema=_build_zone_select_schema(
                self._zone_options, self._preselected
            ),
        )

    async def async_step_iwr_zones_manual(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Manually select zones from all 12 options."""
        if user_input is not None:
            self._connection_data["zones"] = _parse_zone_selection(user_input)
            return await self._async_create_entry(self._connection_data)

        self._zone_options = [
            SelectOptionDict(value=str(z), label=f"Zone {z}") for z in range(1, 13)
        ]

        return self.async_show_form(
            step_id="iwr_zones_manual",
            data_schema=_build_zone_select_schema(self._zone_options, []),
        )

    async def _async_create_entry(
        self, connection_data: dict[str, Any]
    ) -> ConfigFlowResult:
        """Create a config entry from validated connection data."""
        device_type = self._device_type.value
        unique_id = f"broetje_{device_type}_{connection_data[CONF_HOST]}_{connection_data[CONF_UNIT_ID]}"
        await self.async_set_unique_id(unique_id)
        self._abort_if_unique_id_configured()

        model_name = DEVICE_MODELS[self._device_type]
        data = {**connection_data, CONF_DEVICE_TYPE: device_type}

        return self.async_create_entry(
            title=f"Brötje {model_name} ({connection_data[CONF_HOST]})",
            data=data,
        )

    async def _test_connection(self, host: str, port: int, unit_id: int) -> None:
        """Test if we can connect to the Modbus device."""
        from pymodbus.client import AsyncModbusTcpClient

        client = AsyncModbusTcpClient(host=host, port=port)

        try:
            _LOGGER.debug("Attempting to connect to %s:%s", host, port)

            connected = await client.connect()
            if not connected:
                _LOGGER.error("Failed to connect to %s:%s", host, port)
                raise CannotConnect(f"Failed to connect to {host}:{port}")

            _LOGGER.info("Connection test successful for %s:%s", host, port)

        except OSError as err:
            _LOGGER.error("OS error during connection test: %s", err)
            raise CannotConnect(str(err)) from err
        finally:
            client.close()
