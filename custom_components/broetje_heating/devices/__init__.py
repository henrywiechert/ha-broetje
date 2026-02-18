"""Device type definitions for Brötje Heating Systems."""

from __future__ import annotations

from enum import StrEnum
from typing import Any, Final

CONF_DEVICE_TYPE: Final = "device_type"


class DeviceType(StrEnum):
    """Supported Brötje device types."""

    ISR = "isr"
    IWR = "iwr"


DEVICE_MODELS: Final[dict[DeviceType, str]] = {
    DeviceType.ISR: "ISR",
    DeviceType.IWR: "IWR/GTW-08",
}


def get_device_config(
    device_type: DeviceType | str, zones: list[int] | None = None
) -> dict[str, Any]:
    """Return register_map, sensors, binary_sensors, enum_maps for a device type."""
    device_type = DeviceType(device_type)

    if device_type == DeviceType.ISR:
        from .isr import (
            ISR_BINARY_SENSORS,
            ISR_ENTITY_CLASSIFICATION,
            ISR_ENUM_MAPS,
            ISR_REGISTER_MAP,
            ISR_SENSORS,
        )

        return {
            "register_map": ISR_REGISTER_MAP,
            "sensors": ISR_SENSORS,
            "binary_sensors": ISR_BINARY_SENSORS,
            "enum_maps": ISR_ENUM_MAPS,
            "entity_classification": ISR_ENTITY_CLASSIFICATION,
        }

    if device_type == DeviceType.IWR:
        from .iwr import get_iwr_device_config

        return get_iwr_device_config(zones=zones)

    msg = f"Unknown device type: {device_type}"
    raise ValueError(msg)
