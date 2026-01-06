# Supported Entities

This document lists all entities provided by the Brötje Heatpump integration.

## Heating Circuit 1 (Heizkreis 1)

### Sensors

| Entity | Description | Register | Unit | R/W |
|--------|-------------|----------|------|-----|
| HC1 Operating mode | Operating mode (Protection/Auto/Reduced/Comfort) | 1024 | - | R/W |
| HC1 Comfort setpoint | Comfort mode room temperature setpoint | 1025 | °C | R/W |
| HC1 Reduced setpoint | Reduced mode room temperature setpoint | 1026 | °C | R/W |
| HC1 Frost protection setpoint | Frost protection temperature | 1027 | °C | R/W |
| HC1 Heating curve slope | Heating curve steepness (0.1 - 4.0) | 1028 | - | R/W |
| HC1 Heating curve offset | Heating curve parallel shift | 1029 | °C | R/W |
| HC1 Summer/Winter threshold | Outside temp threshold for summer mode | 1030 | °C | R/W |
| HC1 Day heating threshold | Day heating limit temperature | 1032 | °C | R/W |
| HC1 Flow setpoint minimum | Minimum flow temperature setpoint | 1034 | °C | R/W |
| HC1 Flow setpoint maximum | Maximum flow temperature setpoint | 1035 | °C | R/W |
| HC1 Flow setpoint room thermostat | Flow setpoint when using room thermostat | 1036 | °C | R/W |
| HC1 Room influence | Room temperature influence factor | 1038 | % | R/W |
| HC1 Room temperature | Current room temperature | 1042 | °C | R |
| HC1 Room setpoint | Current room temperature setpoint | 1044 | °C | R |
| HC1 Flow temperature | Current flow temperature | 1046 | °C | R |
| HC1 Flow setpoint | Current flow temperature setpoint | 1048 | °C | R |
| HC1 Status | Heating circuit status code | 1054 | - | R |
| HC1 Mixer boost | Mixer overshoot temperature | 1077 | °C | R/W |
| HC1 Pump speed | Current pump speed | 1101 | % | R |
| HC1 Pump speed minimum | Minimum pump speed setting | 1128 | % | R/W |
| HC1 Pump speed maximum | Maximum pump speed setting | 1129 | % | R/W |

### Binary Sensors

| Entity | Description | Register | Values |
|--------|-------------|----------|--------|
| HC1 Enabled | Heating circuit active | 1055 | 0=Off, 1=On |
| HC1 Pump | Heating circuit pump running | 1095 | 0=Off, 1=On |
| HC1 Mixer open | Mixer valve opening | 1097 | 0=Off, 1=On |
| HC1 Mixer close | Mixer valve closing | 1099 | 0=Off, 1=On |
| HC1 Room thermostat demand | Heat demand from room thermostat | 1050 | 0=No demand, 1=Demand |

## Operating Modes (Betriebsart)

| Value | German | English |
|-------|--------|---------|
| 0 | Schutzbetrieb | Protection |
| 1 | Automatik | Automatic |
| 2 | Reduziert | Reduced |
| 3 | Komfort | Comfort |

## Scale Factors

The following scale factors are used to convert raw register values:

| Factor | Value | Used for |
|--------|-------|----------|
| Temperature | 1/64 (0.015625) | All temperature values |
| Heating curve slope | 1/50 (0.02) | Heating curve steepness |

## Entity Naming

Entity IDs follow the pattern:
- Sensors: `sensor.broetje_heatpump_<entity_key>`
- Binary sensors: `binary_sensor.broetje_heatpump_<entity_key>`

Example: `sensor.broetje_heatpump_hc1_flow_temperature`

## Future Entities

The following entities are planned for future versions:

- Domestic Hot Water (DHW / Warmwasser)
- Heatpump specific sensors (compressor, outdoor unit)
- Additional heating circuits (HC2, HC3)
- Error codes and diagnostics
