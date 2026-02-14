"""Sensor platform for the Brötje Heatpump integration."""

from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    PERCENTAGE,
    UnitOfEnergy,
    UnitOfPower,
    UnitOfPressure,
    UnitOfTemperature,
    UnitOfTime,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .coordinator import BroetjeModbusCoordinator
from .entity import BroetjeEntity

# Map device class strings to actual classes
DEVICE_CLASS_MAP = {
    "temperature": SensorDeviceClass.TEMPERATURE,
    "pressure": SensorDeviceClass.PRESSURE,
    "power": SensorDeviceClass.POWER,
    "energy": SensorDeviceClass.ENERGY,
    "frequency": SensorDeviceClass.FREQUENCY,
    "duration": SensorDeviceClass.DURATION,
    "enum": SensorDeviceClass.ENUM,
}

# Map unit strings to actual units
UNIT_MAP = {
    "°C": UnitOfTemperature.CELSIUS,
    "bar": UnitOfPressure.BAR,
    "kWh": UnitOfEnergy.KILO_WATT_HOUR,
    "kW": UnitOfPower.KILO_WATT,
    "h": UnitOfTime.HOURS,
    "%": PERCENTAGE,
}

# Map state class strings to actual classes
STATE_CLASS_MAP = {
    "measurement": SensorStateClass.MEASUREMENT,
    "total": SensorStateClass.TOTAL,
    "total_increasing": SensorStateClass.TOTAL_INCREASING,
}


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the sensor platform."""
    coordinator: BroetjeModbusCoordinator = entry.runtime_data

    entities: list[BroetjeSensor] = []

    for sensor_key, sensor_config in coordinator.sensors.items():
        entities.append(
            BroetjeSensor(
                coordinator=coordinator,
                entity_key=sensor_key,
                sensor_config=sensor_config,
            )
        )

    async_add_entities(entities)


class BroetjeSensor(BroetjeEntity, SensorEntity):
    """Sensor entity for Brötje Heatpump."""

    def __init__(
        self,
        coordinator: BroetjeModbusCoordinator,
        entity_key: str,
        sensor_config: dict,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator, entity_key)

        self._register_key = sensor_config["register"]
        self._attr_translation_key = sensor_config.get("translation_key", entity_key)

        # Support zone number placeholders in translation strings
        if zone_number := sensor_config.get("zone_number"):
            self._attr_translation_placeholders = {"zone": str(zone_number)}

        self._attr_device_class = None
        self._enum_map = None

        device_class = sensor_config.get("device_class")

        if device_class == "enum":
            self._attr_device_class = SensorDeviceClass.ENUM
            enum_map_name = sensor_config.get("enum_map", "operating_modes")
            self._enum_map = coordinator.enum_maps.get(enum_map_name, {})
            self._attr_options = list(self._enum_map.values())
        elif device_class:
            self._attr_device_class = DEVICE_CLASS_MAP.get(device_class)

        # Set unit
        unit = sensor_config.get("unit")
        if unit:
            self._attr_native_unit_of_measurement = UNIT_MAP.get(unit, unit)

        # Set state class
        state_class = sensor_config.get("state_class")
        if state_class:
            self._attr_state_class = STATE_CLASS_MAP.get(state_class)

        # Set icon if specified
        if icon := sensor_config.get("icon"):
            self._attr_icon = icon

    @property
    def native_value(self) -> float | str | None:
        """Return the sensor value."""
        if self.coordinator.data is None:
            return None

        value = self.coordinator.data.get(self._register_key)

        if value is None:
            return None

        # Handle enum device class - return None for unmapped values
        # to avoid HA rejecting states not in the options list
        if self._attr_device_class == SensorDeviceClass.ENUM and self._enum_map:
            return self._enum_map.get(int(value))

        # Round temperature values to 1 decimal
        if self._attr_device_class == SensorDeviceClass.TEMPERATURE:
            return round(value, 1)

        # Round pressure values to 2 decimals
        if self._attr_device_class == SensorDeviceClass.PRESSURE:
            return round(value, 2)

        # Round other numeric values to 2 decimals
        if isinstance(value, float):
            return round(value, 2)

        return value
