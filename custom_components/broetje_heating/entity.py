"""Base entity for the Brötje Heatpump integration."""

from __future__ import annotations

from typing import Any

from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, SUB_DEVICE_LABELS
from .coordinator import BroetjeModbusCoordinator


class BroetjeEntity(CoordinatorEntity[BroetjeModbusCoordinator]):
    """Base class for Brötje Heatpump entities."""

    _attr_has_entity_name = True
    _register_key: str | None = None

    def __init__(
        self,
        coordinator: BroetjeModbusCoordinator,
        entity_key: str,
        zone_number: int | None = None,
        sub_device: str | None = None,
    ) -> None:
        """Initialize the entity."""
        super().__init__(coordinator)
        self._entity_key = entity_key
        self._zone_number = zone_number
        self._sub_device = sub_device

        # Generate unique ID based on device and entity key
        device_id = (
            coordinator.config_entry.unique_id or coordinator.config_entry.entry_id
        )
        self._attr_unique_id = f"{device_id}_{entity_key}"

        # Apply entity classification (category + enabled_default)
        category, enabled = coordinator.entity_classification.get(
            entity_key, (None, True)
        )
        if category == "diagnostic":
            self._attr_entity_category = EntityCategory.DIAGNOSTIC
        self._attr_entity_registry_enabled_default = enabled

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information, routing zone entities to sub-devices."""
        entry_id = self.coordinator.config_entry.entry_id

        if self._zone_number is not None:
            return DeviceInfo(
                identifiers={(DOMAIN, f"{entry_id}_zone_{self._zone_number}")},
                name=f"Brötje Zone {self._zone_number}",
                manufacturer=self.coordinator.device_manufacturer,
                model=self.coordinator.device_model,
                via_device=(DOMAIN, entry_id),
            )

        if self._sub_device is not None:
            label = SUB_DEVICE_LABELS.get(
                self._sub_device, self._sub_device.replace("_", " ").title()
            )
            return DeviceInfo(
                identifiers={(DOMAIN, f"{entry_id}_{self._sub_device}")},
                name=f"Brötje {self.coordinator.device_model} – {label}",
                manufacturer=self.coordinator.device_manufacturer,
                model=self.coordinator.device_model,
                via_device=(DOMAIN, entry_id),
            )

        return DeviceInfo(
            identifiers={(DOMAIN, entry_id)},
            name=f"Brötje {self.coordinator.device_model}",
            manufacturer=self.coordinator.device_manufacturer,
            model=self.coordinator.device_model,
            serial_number=self.coordinator.device_serial,
            sw_version=self.coordinator.device_firmware,
        )

    @property
    def extra_state_attributes(self) -> dict[str, Any] | None:
        """Return register metadata as extra state attributes."""
        if self._register_key is None:
            return None

        reg_config = self.coordinator.register_map.get(self._register_key)
        if reg_config is None:
            return None

        attrs: dict[str, Any] = {
            "register_address": reg_config["address"],
            "register_type": reg_config.get("type", "holding"),
            "register_size": reg_config.get("count", 1),
            "data_type": reg_config.get("data_type", "int16"),
        }

        scale = reg_config.get("scale", 1)
        if scale != 1:
            attrs["scaling_factor"] = scale

        if bit := reg_config.get("bit"):
            attrs["bit_position"] = bit

        return attrs
