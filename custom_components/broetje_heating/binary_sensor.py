"""Binary sensor platform for the Brötje Heatpump integration."""

from __future__ import annotations

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import BINARY_SENSORS
from .coordinator import BroetjeModbusCoordinator
from .entity import BroetjeEntity


# Map device class strings to actual classes
DEVICE_CLASS_MAP = {
    "running": BinarySensorDeviceClass.RUNNING,
    "problem": BinarySensorDeviceClass.PROBLEM,
    "heat": BinarySensorDeviceClass.HEAT,
    "cold": BinarySensorDeviceClass.COLD,
    "power": BinarySensorDeviceClass.POWER,
}


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the binary sensor platform."""
    coordinator: BroetjeModbusCoordinator = entry.runtime_data

    entities: list[BroetjeBinarySensor] = []

    for sensor_key, sensor_config in BINARY_SENSORS.items():
        entities.append(
            BroetjeBinarySensor(
                coordinator=coordinator,
                entity_key=sensor_key,
                sensor_config=sensor_config,
            )
        )

    async_add_entities(entities)


class BroetjeBinarySensor(BroetjeEntity, BinarySensorEntity):
    """Binary sensor entity for Brötje Heatpump."""

    def __init__(
        self,
        coordinator: BroetjeModbusCoordinator,
        entity_key: str,
        sensor_config: dict,
    ) -> None:
        """Initialize the binary sensor."""
        super().__init__(coordinator, entity_key)

        self._register_key = sensor_config["register"]
        self._attr_translation_key = sensor_config.get("translation_key", entity_key)

        # Set device class
        device_class = sensor_config.get("device_class")
        if device_class:
            self._attr_device_class = DEVICE_CLASS_MAP.get(device_class)

        # Set icon if specified
        if icon := sensor_config.get("icon"):
            self._attr_icon = icon

    @property
    def is_on(self) -> bool | None:
        """Return true if the binary sensor is on."""
        if self.coordinator.data is None:
            return None

        value = self.coordinator.data.get(self._register_key)

        if value is None:
            return None

        return bool(value)
