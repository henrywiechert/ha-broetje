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

from .const import (
    CONF_SCAN_INTERVAL,
    CONF_UNIT_ID,
    DEFAULT_PORT,
    DEFAULT_SCAN_INTERVAL,
    DEFAULT_UNIT_ID,
    DOMAIN,
)
from .devices import CONF_DEVICE_TYPE, DEVICE_MODELS, DeviceType

_LOGGER = logging.getLogger(__name__)

STEP_CONNECTION_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_HOST): str,
        vol.Required(CONF_PORT, default=DEFAULT_PORT): int,
        vol.Required(CONF_UNIT_ID, default=DEFAULT_UNIT_ID): int,
    }
)

STEP_IWR_ZONES_SCHEMA = vol.Schema(
    {
        vol.Required("zone_count", default=1): vol.All(int, vol.Range(min=1, max=12)),
    }
)


class CannotConnect(Exception):
    """Error to indicate we cannot connect."""


class BroetjeOptionsFlow(OptionsFlow):
    """Handle options for Brötje Heatpump."""

    async def async_step_init(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(data=user_input)

        current_interval = self.config_entry.options.get(
            CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL
        )

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_SCAN_INTERVAL, default=current_interval
                    ): vol.All(int, vol.Range(min=10, max=3600)),
                }
            ),
        )


class BroetjeHeatpumpConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Brötje Heatpump."""

    VERSION = 2
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
                # For IWR, proceed to zone configuration step
                if self._device_type == DeviceType.IWR:
                    self._connection_data = user_input
                    return await self.async_step_iwr_zones()

                # For ISR, create entry directly
                return await self._async_create_entry(user_input)

        return self.async_show_form(
            step_id=self._device_type.value,
            data_schema=STEP_CONNECTION_DATA_SCHEMA,
            errors=errors,
        )

    async def async_step_iwr_zones(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle IWR zone count selection."""
        if user_input is not None:
            self._connection_data["zone_count"] = user_input["zone_count"]
            return await self._async_create_entry(self._connection_data)

        return self.async_show_form(
            step_id="iwr_zones",
            data_schema=STEP_IWR_ZONES_SCHEMA,
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
