"""Config flow for Brötje Heatpump integration."""

from __future__ import annotations

import asyncio
import logging
from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_HOST, CONF_PORT

from .const import (
    CONF_UNIT_ID,
    DEFAULT_PORT,
    DEFAULT_UNIT_ID,
    DOMAIN,
)

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_HOST): str,
        vol.Required(CONF_PORT, default=DEFAULT_PORT): int,
        vol.Required(CONF_UNIT_ID, default=DEFAULT_UNIT_ID): int,
    }
)


class CannotConnect(Exception):
    """Error to indicate we cannot connect."""


class BroetjeHeatpumpConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Brötje Heatpump."""

    VERSION = 1
    MINOR_VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
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
                # Generate unique ID from host (will be replaced with serial if available)
                unique_id = f"broetje_{user_input[CONF_HOST]}_{user_input[CONF_UNIT_ID]}"
                await self.async_set_unique_id(unique_id)
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=f"Brötje Heatpump ({user_input[CONF_HOST]})",
                    data=user_input,
                )

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
        )

    async def _test_connection(self, host: str, port: int, unit_id: int) -> None:
        """Test if we can connect to the Modbus device."""
        from pymodbus.client import AsyncModbusTcpClient
        from pymodbus.exceptions import ModbusException

        client = AsyncModbusTcpClient(host=host, port=port)
        
        try:
            _LOGGER.debug("Attempting to connect to %s:%s", host, port)
            
            connected = await client.connect()
            if not connected:
                _LOGGER.error("Failed to connect to %s:%s", host, port)
                raise CannotConnect(f"Failed to connect to {host}:{port}")
            
            _LOGGER.debug("Connected successfully, testing register read with unit_id=%s", unit_id)
            
            # Try to read a register to verify communication
            # Using input register 0 as a basic connectivity test
            try:
                async with asyncio.timeout(5):
                    result = await client.read_input_registers(
                        address=0,
                        count=1,
                        slave=unit_id,
                    )
                
                if hasattr(result, 'isError') and result.isError():
                    _LOGGER.warning(
                        "Modbus read error during connection test (this may be normal): %s",
                        result
                    )
                else:
                    _LOGGER.debug("Register read successful: %s", result)
                    
            except TimeoutError:
                _LOGGER.warning("Register read timed out (connection may still be valid)")
                
            # Connection works - register read failures are acceptable at this stage
            # since we don't know the exact register addresses yet
            _LOGGER.info("Connection test successful for %s:%s", host, port)
                
        except ModbusException as err:
            _LOGGER.error("Modbus exception during connection test: %s", err)
            raise CannotConnect(str(err)) from err
        except OSError as err:
            _LOGGER.error("OS error during connection test: %s", err)
            raise CannotConnect(str(err)) from err
        finally:
            client.close()
