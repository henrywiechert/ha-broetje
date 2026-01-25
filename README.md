# Brötje Heating System Integration for Home Assistant

🇩🇪 [Deutsche Version](README.de.md)

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![GitHub Release](https://img.shields.io/github/v/release/henrywiechert/ha-broetje)](https://github.com/henrywiechert/ha-broetje/releases)

<img src="custom_components/broetje_heatpump/images/logo.png" alt="Brötje Logo" width="200">

Home Assistant integration for Brötje heatpumps (and other heating systems) via Modbus TCP (ISR MBM, IWR under check)

Currently only the ISR controller (mainly for gas heating) is supported. IWR, used in heatpumps will follow. 
In my tests so far, I had a ISR controller connected to the heatpump BLW Eco 10.1. It generally works, but misses a few heatpump specific measurements. IWR connection is going to come soon (GTW-08).

## Supported Models

<img src="custom_components/broetje_heatpump/images/Broetje-BLW-Eco-10.1.png" alt="Brötje BLW Eco" width="300">

**Brötje BLW Eco 10.1** (tested)

*Other Brötje heatpumps with Modbus interface may also work.*


## Features

> **Note:** All information is derived from this Brötje document:
[de-de_ma_modbm.pdf](https://polo.broetje.de/pdf/7715040=6=pdf_(bdr_a4_manual)=de-de_ma_modbm.pdf)

- **ISR module only**
- **Read-only monitoring** (v0.2)
- **about 100 entities** across 6 categories
- **German and English translations**
- 30-second polling interval

### Supported Categories

| Category | Sensors | Binary Sensors | Description |
|----------|---------|----------------|-------------|
| **Heating Circuit 1** (Heizkreis 1) | 21 | 5 | Temperatures, setpoints, pump, mixer |
| **DHW Settings** (Trinkwasser) | 12 | - | Operating mode, legionella, circulation |
| **DHW Storage Tank** (Trinkwasserspeicher) | 11 | 3 | Tank temperatures, pumps |
| **Buffer Storage** (Pufferspeicher) | 5 | 2 | Buffer temperatures, valves |
| **Boiler** (Kessel) | 31 | 3 | Burner, fan, energy counters |
| **General Functions** (Allgemein) | 3 | 4 | Outdoor temp, alarm, manual mode |

> ⚠️ **Note:** Currently only **Heating Circuit 1 (Heizkreis 1)** is supported. Support for HC2/HC3 may be added in future versions.

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
5. Add `https://github.com/henrywiechert/ha-broetje` and select "Integration" as the category
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

## Entities

See [ENTITIES.md](ENTITIES.md) for a complete list of all 100 entities with their Modbus register addresses and descriptions.

### Highlights


- **Temperatures**: Flow, return, room, boiler, buffer, DHW
- **Energy counters**: Gas consumption for heating and DHW (kWh)
- **Operating hours**: Burner hours, heating hours, DHW hours
- **Status information**: Boiler status, burner status, pump states
- **Configuration**: Heating curve, setpoints, operating modes

Not every sensor is available on every heating system! E.g. gas consumption on heat pumps :-)

## Dashboard Example

```yaml
type: picture-glance
image: /local/broetje_heatpump/Broetje-BLW-Eco-10.1.png
title: Brötje Wärmepumpe
entities:
  - entity: sensor.brotje_heatpump_hc1_flow_temperature
    name: Vorlauf
  - entity: sensor.brotje_heatpump_kesseltemperatur
    name: Kessel
  - entity: sensor.brotje_heatpump_aussentemperatur
    name: Außen
  - entity: binary_sensor.brotje_heatpump_hc1_pump
    name: Pumpe
```

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

- [pymodbus](https://pymodbus.readthedocs.io/) ≥3.11.0 for Modbus TCP communication
- Home Assistant's `DataUpdateCoordinator` for efficient polling

### Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request


## Roadmap

- [ ] Write support for R/W registers
- [ ] Additional heating circuits (HC2, HC3)
- [ ] Heatpump specific sensors
- [ ] Error codes and diagnostics
- [ ] Brötje logo in official HA brand repo

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This integration is not affiliated with or endorsed by Brötje. Use at your own risk.
