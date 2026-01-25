"""Base entity for the Brötje Heatpump integration."""

from __future__ import annotations

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import BroetjeModbusCoordinator


class BroetjeEntity(CoordinatorEntity[BroetjeModbusCoordinator]):
    """Base class for Brötje Heatpump entities."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: BroetjeModbusCoordinator,
        entity_key: str,
    ) -> None:
        """Initialize the entity."""
        super().__init__(coordinator)
        self._entity_key = entity_key

        # Generate unique ID based on device and entity key
        device_id = (
            coordinator.config_entry.unique_id or coordinator.config_entry.entry_id
        )
        self._attr_unique_id = f"{device_id}_{entity_key}"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self.coordinator.config_entry.entry_id)},
            name="Brötje Heatpump",
            manufacturer=self.coordinator.device_manufacturer,
            model=self.coordinator.device_model,
            serial_number=self.coordinator.device_serial,
            sw_version=self.coordinator.device_firmware,
        )
