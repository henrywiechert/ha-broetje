"""Climate platform for the Brötje Heatpump integration."""

from __future__ import annotations

from typing import ClassVar

from homeassistant.components.climate import (
    ClimateEntity,
    ClimateEntityFeature,
    HVACAction,
    HVACMode,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE, UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .coordinator import BroetjeModbusCoordinator
from .entity import BroetjeEntity

# IWR zone control mode register values (CP32X)
_ZONE_CONTROL_MANUAL = 1
_ZONE_CONTROL_OFF = 2

# IWR zone heating mode register values (CM110)
_HEATING_MODE_STANDBY = 0
_HEATING_MODE_HEATING = 1
_HEATING_MODE_COOLING = 2


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the climate platform."""
    coordinator: BroetjeModbusCoordinator = entry.runtime_data

    async_add_entities(
        BroetjeClimate(coordinator=coordinator, entity_key=key, climate_config=cfg)
        for key, cfg in coordinator.climates.items()
    )


class BroetjeClimate(BroetjeEntity, ClimateEntity):
    """Climate entity representing a Brötje heating zone thermostat."""

    _attr_hvac_modes: ClassVar = [HVACMode.HEAT, HVACMode.OFF]
    _attr_supported_features = ClimateEntityFeature.TARGET_TEMPERATURE
    _attr_temperature_unit = UnitOfTemperature.CELSIUS
    _attr_target_temperature_step = 0.5
    _attr_min_temp = 5.0
    _attr_max_temp = 30.0

    def __init__(
        self,
        coordinator: BroetjeModbusCoordinator,
        entity_key: str,
        climate_config: dict,
    ) -> None:
        """Initialize the climate entity."""
        super().__init__(
            coordinator,
            entity_key,
            zone_number=climate_config.get("zone_number"),
        )

        self._temperature_register = climate_config["temperature_register"]
        self._setpoint_register = climate_config["setpoint_register"]
        self._control_mode_register = climate_config["control_mode_register"]
        self._heating_mode_register = climate_config["heating_mode_register"]

        self._attr_translation_key = climate_config.get("translation_key", entity_key)

        if zone_number := climate_config.get("zone_number"):
            self._attr_translation_placeholders = {"zone": str(zone_number)}

        # Apply min/max/step from the register map if present
        if setpoint_reg := coordinator.register_map.get(self._setpoint_register):
            if "min" in setpoint_reg:
                self._attr_min_temp = float(setpoint_reg["min"])
            if "max" in setpoint_reg:
                self._attr_max_temp = float(setpoint_reg["max"])
            if "step" in setpoint_reg:
                self._attr_target_temperature_step = float(setpoint_reg["step"])

    @property
    def current_temperature(self) -> float | None:
        """Return the current measured room temperature."""
        if self.coordinator.data is None:
            return None
        value = self.coordinator.data.get(self._temperature_register)
        if value is None:
            return None
        return round(float(value), 1)

    @property
    def target_temperature(self) -> float | None:
        """Return the manual room temperature setpoint."""
        if self.coordinator.data is None:
            return None
        value = self.coordinator.data.get(self._setpoint_register)
        if value is None:
            return None
        return round(float(value), 1)

    @property
    def hvac_mode(self) -> HVACMode:
        """Return current HVAC mode based on zone control mode register."""
        if self.coordinator.data is None:
            return HVACMode.OFF
        control_mode = self.coordinator.data.get(self._control_mode_register)
        if control_mode is None or int(control_mode) == _ZONE_CONTROL_OFF:
            return HVACMode.OFF
        return HVACMode.HEAT

    @property
    def hvac_action(self) -> HVACAction:
        """Return the current running HVAC action."""
        if self.hvac_mode == HVACMode.OFF:
            return HVACAction.OFF
        if self.coordinator.data is None:
            return HVACAction.IDLE
        heating_mode = self.coordinator.data.get(self._heating_mode_register)
        if heating_mode is None:
            return HVACAction.IDLE
        mode = int(heating_mode)
        if mode == _HEATING_MODE_HEATING:
            return HVACAction.HEATING
        if mode == _HEATING_MODE_COOLING:
            return HVACAction.COOLING
        return HVACAction.IDLE

    async def async_set_temperature(self, **kwargs) -> None:
        """Set a new target temperature."""
        temperature = kwargs.get(ATTR_TEMPERATURE)
        if temperature is None:
            return
        await self.coordinator.async_write_register(
            self._setpoint_register, temperature
        )

    async def async_set_hvac_mode(self, hvac_mode: HVACMode) -> None:
        """Set the HVAC mode by writing to the zone control mode register."""
        if hvac_mode == HVACMode.OFF:
            await self.coordinator.async_write_register(
                self._control_mode_register, _ZONE_CONTROL_OFF
            )
        elif hvac_mode == HVACMode.HEAT:
            # Switch to manual mode so the room setpoint takes effect immediately
            await self.coordinator.async_write_register(
                self._control_mode_register, _ZONE_CONTROL_MANUAL
            )
