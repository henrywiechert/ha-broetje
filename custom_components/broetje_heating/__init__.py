"""The Brötje Heatpump integration."""

from __future__ import annotations

import logging
import shutil
from pathlib import Path

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant


from .coordinator import BroetjeModbusCoordinator

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [
    Platform.SENSOR,
    Platform.BINARY_SENSOR,
]

type BroetjeConfigEntry = ConfigEntry[BroetjeModbusCoordinator]


async def async_setup_entry(hass: HomeAssistant, entry: BroetjeConfigEntry) -> bool:
    """Set up Brötje Heatpump from a config entry."""
    # Copy images to www folder for dashboard use
    await hass.async_add_executor_job(_copy_images_to_www, hass)

    coordinator = BroetjeModbusCoordinator(hass, entry)

    await coordinator.async_config_entry_first_refresh()

    entry.runtime_data = coordinator

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


def _copy_images_to_www(hass: HomeAssistant) -> None:
    """Copy integration images to www folder for dashboard use."""
    source_dir = Path(__file__).parent / "images"
    www_dir = Path(hass.config.path("www")) / "broetje_heatpump"

    if not source_dir.exists():
        _LOGGER.debug("No images directory found in integration")
        return

    try:
        www_dir.mkdir(parents=True, exist_ok=True)

        for image_file in source_dir.glob("*.png"):
            dest_file = www_dir / image_file.name
            if not dest_file.exists():
                shutil.copy2(image_file, dest_file)
                _LOGGER.debug("Copied %s to %s", image_file.name, dest_file)

        _LOGGER.info("Images available at /local/broetje_heatpump/ for dashboard use")
    except OSError as err:
        _LOGGER.warning("Failed to copy images to www folder: %s", err)


async def async_unload_entry(hass: HomeAssistant, entry: BroetjeConfigEntry) -> bool:
    """Unload a config entry."""
    if unload_ok := await hass.config_entries.async_unload_platforms(entry, PLATFORMS):
        await entry.runtime_data.async_shutdown()

    return unload_ok
