# Brötje Heatpump Integration for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)

<img src="custom_components/broetje_heatpump/images/logo.png" alt="Brötje Logo" width="200">

Home Assistant integration for Brötje heatpumps via Modbus TCP.

## Supported Models

<img src="custom_components/broetje_heatpump/images/Broetje-BLW-Eco-10.1.png" alt="Brötje BLW Eco" width="300">

- **Brötje BLW Eco 10.1** (tested)

*Other Brötje heatpumps with Modbus interface may also work.*

## Features

- **Read-only monitoring** (v0.1)
  - Heating circuit temperatures and setpoints
  - Operating mode (Protection/Auto/Reduced/Comfort)
  - Heating curve parameters
  - Pump and mixer states
  - Room temperature and setpoints

## Requirements

- Brötje heatpump with Modbus interface
- Modbus TCP gateway connected to the heatpump
- Home Assistant 2024.1.0 or newer

## Installation

### HACS (Recommended)

1. Open HACS in Home Assistant
2. Click on "Integrations"
3. Click the three dots in the top right corner
4. Select "Custom repositories"
5. Add this repository URL and select "Integration" as the category
6. Click "Add"
7. Search for "Brötje Heatpump" and install it
8. Restart Home Assistant

### Manual Installation

1. Download the `custom_components/broetje_heatpump` folder
2. Copy it to your Home Assistant `config/custom_components/` directory
3. Restart Home Assistant

## Configuration

1. Go to **Settings** → **Devices & Services**
2. Click **Add Integration**
3. Search for "Brötje Heatpump"
4. Enter the connection details:
   - **Host**: IP address of your Modbus TCP gateway
   - **Port**: Modbus TCP port (default: 502)
   - **Unit ID**: Modbus slave ID (default: 1)

## Dashboard

The integration automatically copies images to `/local/broetje_heatpump/` for use in your dashboard.

### Picture Glance Card Example

```yaml
type: picture-glance
image: /local/broetje_heatpump/Broetje-BLW-Eco-10.1.png
title: Brötje Wärmepumpe
entities:
  - entity: sensor.broetje_heatpump_hc1_flow_temperature
    name: Vorlauf
  - entity: sensor.broetje_heatpump_hc1_room_temperature
    name: Raum
  - entity: binary_sensor.broetje_heatpump_hc1_pump
    name: Pumpe
```

## Entities

See [ENTITIES.md](ENTITIES.md) for a complete list of all supported sensors and binary sensors with their Modbus register addresses.

**Summary:**
- 21 Sensors (temperatures, setpoints, operating mode, pump speed)
- 5 Binary Sensors (pump, mixer, thermostat demand)

## Troubleshooting

### Cannot connect to device

- Verify the Modbus TCP gateway is accessible from Home Assistant
- Check the IP address and port are correct
- Ensure the Modbus unit ID matches your device configuration
- Test connectivity using a Modbus tool like `mbpoll`

### No sensor values

- The register addresses may need adjustment for your specific model
- Check Home Assistant logs for Modbus communication errors

## Development

This integration uses:

- [pymodbus](https://pymodbus.readthedocs.io/) for Modbus TCP communication
- Home Assistant's `DataUpdateCoordinator` for efficient polling

### Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This integration is not affiliated with or endorsed by Brötje. Use at your own risk.
