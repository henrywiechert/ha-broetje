# Brötje Heating System Integration for Home Assistant

🇩🇪 [Deutsche Version](README.de.md)

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![GitHub Release](https://img.shields.io/github/v/release/henrywiechert/ha-broetje)](https://github.com/henrywiechert/ha-broetje/releases)

<img src="custom_components/broetje_heating/images/logo.png" alt="Brötje Logo" width="200">

Home Assistant integration for Brötje heating systems via Modbus TCP, supporting both the **IWR/GTW-08** gateway (heat pumps) and the **ISR Plus** module (gas boilers and older systems).

## Supported Modules

This integration supports two Brötje Modbus modules. During installation, you select which module your system uses. Both can be installed in parallel if you have multiple heating appliances.

| Module | Type | Typical Use | Status |
|--------|------|-------------|--------|
| **IWR / GTW-08** | Gateway module | Heat pumps, newer systems | Supported |
| **ISR Plus** | Modbus module | Gas boilers, older systems | Supported |

### IWR / GTW-08 (Gateway Module)

The IWR/GTW-08 is the current-generation Modbus gateway used by Brötje heat pumps and newer heating systems. It provides comprehensive monitoring including:

- Appliance temperatures, pressures, and power
- Heat pump status (main status + sub status with 100+ codes)
- Energy counters (consumed and delivered, per CH/DHW/cooling)
- COP monitoring
- Up to 12 configurable zones with per-zone temperatures, setpoints, and pump status
- Bitfield-based status indicators (flame, heat pump, backup heaters, valves)
- Service and error diagnostics per board

Register specifications:
- GTW-08 Modbus (7854678 - v.01) — English
- Modbus GTW-08 Parameter List (7740782-01) — German

### ISR Plus (Legacy Module)

The ISR Plus module is the older Modbus interface found on Brötje gas boilers and some heat pump installations. It provides:

- Heating circuit 1 temperatures and setpoints
- DHW (domestic hot water) settings and tank status
- Buffer storage monitoring
- Boiler/burner status and energy counters
- General functions (outdoor temperature, alarm relay)

Register specification: [de-de_ma_modbm.pdf](https://polo.broetje.de/pdf/7715040=6=pdf_(bdr_a4_manual)=de-de_ma_modbm.pdf)

## Supported Models
All Brötje heatpumps and gasboilers with one of the listed Modbus interfaces.

<img src="custom_components/broetje_heating/images/Broetje-BLW-Eco-10.1.png" alt="Brötje BLW Eco" width="300">

### Tested Models
- **Brötje BLW Eco 10.1** (tested with ISR and IWR/GTW-08)
- **Brötje BLW Eco 12.1**
- **Brötje BLW Mono 8** (Hybrid Setup, Remeha GTW-08)
- **Brötje BLW Eco 6.1** (GTW-08, Waveshare RS485/RJ45 Ethernet Converter)
- **Brötje BLW Mono 6.1**
 
*Other Brötje heating systems with Modbus interface should also work. I appreciate any feedback for other models*

## Features

- **Two module types**: IWR/GTW-08 and ISR Plus, selectable during setup
- **Parallel operation**: Both modules can run side by side for different appliances
- **Read + write support (selected registers)**: Monitoring remains read-focused, with safe write support for selected IWR holding registers exposed as `number`/`select`/`climate` entities
- **IWR**: ~213 entities (1 zone) up to ~884 entities (12 zones) — main appliance, zone parameters & measurements, device info, service, error diagnostics
- **ISR**: 117 entities (100 sensors + 17 binary sensors) across 6 categories
- **Zone detection** (IWR): Automatically detects active zones by reading zone type and function registers from the device; active zones are pre-selected, inactive ones shown but unchecked. Manual selection also available.
- **Climate subsystem** (IWR): Zone thermostat entities are exposed via Home Assistant `climate` entities (Thermostat card compatible) with current temperature, target setpoint, and HVAC mode/action mapping.
- **Writable zone controls** (IWR): Write-enabled entities for selected zone registers, including control mode, room setpoint (manual), room temperature measured (external sensor injection), DHW calorifier hysteresis, and DHW comfort/reduced/holiday setpoints.
- **Sub-devices**: Entities are grouped under functional sub-devices (for example boiler/service/solar/buffer/hybrid). Only detected sub-devices are kept; stale/orphaned sub-devices are removed automatically on reload.
- **Configurable zones** (IWR): 1–12 zones selectable during setup or reconfigurable via integration options
- **Configurable scan interval**: Adjustable polling interval via integration options (default: 120 seconds)
- **German and English translations**
- **Sentinel value filtering**: Invalid Modbus readings (0xFFFF, 0xFFFFFFFF) are shown as "Unavailable" instead of bogus numbers

### ISR Coverage

- 🌡️ **Heating Circuit 1** — temperatures, setpoints, pump, mixer
- 🚿 **DHW** — operating mode, legionella protection, circulation
- 🪣 **DHW Storage Tank** — tank temperatures, pumps
- 🔋 **Buffer Storage** — buffer temperatures, valves
- 🔥 **Boiler** — burner, fan, energy counters
- ⚙️ **General Functions** — outdoor temperature, alarm relay, manual mode

> **Note:** Currently only **Heating Circuit 1 (HK1)** is supported. Support for HC2/HC3 may be added in a future version.

### IWR Coverage

- 🌡️ **Appliance** — temperatures, pressures, flow/return, COP, power, CH/DHW/cooling enable
- 🎛️ **Main Controller** — status bits, heat demand, output states, energy counters
- 🏠 **Zones** (per zone, up to 12) — setpoints, heating curves, control strategy, time programs, room/flow temperatures, valve and pump states
- 🔧 **System Discovery** — connected boards, device types, software/firmware versions, article numbers
- ⚠️ **Service & Diagnostics** — error codes and severity per board, service notifications
- 🔗 **Cascade** — cascade status

> Entity counts scale with the number of configured zones: ~213 entities for 1 zone, up to ~884 for 12 zones.

## Requirements

- Brötje heating system with Modbus interface
- Modbus TCP gateway connected to the heating system
- Home Assistant 2024.1.0 or newer

## Installation

### HACS (Recommended)

1. Open HACS in Home Assistant
2. Click on "Integrations"
3. Click the three dots in the top right corner
4. Select "Custom repositories"
5. Add `https://github.com/henrywiechert/ha-broetje` and select "Integration" as the category
6. Click "Add"
7. Search for "Brötje" and install it
8. Restart Home Assistant

### Manual Installation

1. Download the `custom_components/broetje_heating` folder
2. Copy it to your Home Assistant `config/custom_components/` directory
3. Restart Home Assistant

## Configuration

1. Go to **Settings** → **Devices & Services**
2. Click **Add Integration**
3. Search for "Brötje"
4. **Select your module type**: ISR or IWR
5. Enter the connection details:
   - **Host**: IP address of your Modbus TCP gateway
   - **Port**: Modbus TCP port (default: 502)
   - **Unit ID**: Modbus slave ID (default: 1)
6. **IWR only**: Choose how to configure zones:
   - **Autodetect**: Reads zone type and function registers from the device; active zones are pre-selected, inactive ones shown but unchecked. Review and confirm the selection.
   - **Manual**: Select any combination of zones 1–12.

To add a second module (e.g., both ISR and IWR), simply add the integration again and select the other module type.

### Options

After setup, click the **Configure** (gear icon) button on the integration entry to adjust:

- **Scan interval**: How often the integration polls the Modbus device (default: 120 seconds, range: 10–3600). Changes take effect immediately without restart.
- **Zone configuration** (IWR only): Re-run autodetection or manually change which zones are active. Changes trigger an integration reload.

## Entities

See [ENTITIES.md](ENTITIES.md) for a complete list of ISR entities with their Modbus register addresses and descriptions.

For IWR entities, see [`custom_components/broetje_heating/register_map.csv`](custom_components/broetje_heating/register_map.csv) for a comprehensive register map including addresses, data types, descriptions (EN/DE), units, scaling factors, and read/write status (`rw_spec` and `rw_implemented`).

### Highlights

- **Temperatures**: Flow, return, room, outdoor, exhaust gas, heat pump
- **Energy counters**: Consumed and delivered energy for CH, DHW, and cooling (kWh)
- **Operating hours**: Total hours, backup heater hours, pump hours per zone
- **Status information**: Main/sub status, pump states, valve positions, flame/heat pump on
- **COP**: Coefficient of performance monitoring (IWR)
- **Diagnostics**: Per-board error codes and severity, service notifications

Not every sensor is available on every heating system! E.g., gas consumption on heat pumps, or COP on gas boilers.

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
- Some sensors show "Unavailable" when the appliance reports sentinel values (0xFFFF) — this is normal for unused features

## Development

This integration uses:

- [pymodbus](https://pymodbus.readthedocs.io/) ≥3.11.0 for Modbus TCP communication
- Home Assistant's `DataUpdateCoordinator` for efficient polling

### Pre-commit hook

A pre-commit hook runs `ruff check` and `ruff format` on `custom_components/broetje_heating` before each commit. To set it up:

```bash
pip install pre-commit
pre-commit install
```

### Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Run `ruff check` and `ruff format --check custom_components/broetje_heating` (or use the pre-commit hook)
4. Submit a pull request

## Roadmap

- [~] Write support for selected R/W registers (ongoing expansion)
- [ ] Additional heating circuits for ISR (HC2, HC3)
- [X] Brötje logo in official HA brand repo

## Acknowledgements

- [@der-seemann](https://github.com/der-seemann) — lot of ideas and feature suggestions

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This integration is not affiliated with or endorsed by Brötje. Use at your own risk.
