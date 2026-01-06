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

## Domestic Hot Water (Trinkwasser / TWW)

### Sensors

| Entity | Description | Register | Unit | R/W |
|--------|-------------|----------|------|-----|
| DHW Operating mode | Operating mode (Off/On/Eco) | 10240 | - | R/W |
| DHW Setpoint | Nominal setpoint temperature (8-80°C) | 10241 | °C | R/W |
| DHW Reduced setpoint | Reduced setpoint temperature (8-80°C) | 10242 | °C | R/W |
| DHW Release mode | Release mode (24h/heating program/DHW program) | 10243 | - | R/W |
| DHW Legionella mode | Legionella function (Off/Periodic/Fixed day) | 10244 | - | R/W |
| DHW Legionella interval | Legionella periodic interval (1-7 days) | 10245 | days | R/W |
| DHW Legionella weekday | Fixed weekday (Monday-Sunday) | 10246 | - | R/W |
| DHW Legionella time | Time of day for legionella function (0-1430 min) | 10247 | min | R/W |
| DHW Legionella setpoint | Legionella temperature setpoint (55-95°C) | 10249 | °C | R/W |
| DHW Legionella dwell time | Dwell time at setpoint (2-360 min) | 10250 | min | R/W |
| DHW Circulation setpoint | Circulation temperature setpoint (8-80°C) | 10263 | °C | R/W |
| DHW Status | DHW status code | 10273 | - | R |

### DHW Operating Modes (TWW Betriebsart)

| Value | German | English |
|-------|--------|---------|
| 0 | Aus | Off |
| 1 | Ein | On |
| 2 | Eco | Eco |

### DHW Release Modes (TWW Freigabe)

| Value | German | English |
|-------|--------|---------|
| 0 | 24h/Tag | 24h/day |
| 1 | Zeitprogramme Heizkreise | Heating circuit program |
| 2 | Zeitprogramm 4/TWW | DHW program |

### Legionella Modes

| Value | German | English |
|-------|--------|---------|
| 0 | Aus | Off |
| 1 | Periodisch | Periodic |
| 2 | Fixer Wochentag | Fixed weekday |

### Weekdays

| Value | German | English |
|-------|--------|---------|
| 1 | Montag | Monday |
| 2 | Dienstag | Tuesday |
| 3 | Mittwoch | Wednesday |
| 4 | Donnerstag | Thursday |
| 5 | Freitag | Friday |
| 6 | Samstag | Saturday |
| 7 | Sonntag | Sunday |

## DHW Storage Tank (Trinkwasserspeicher)

### Sensors

| Entity | Description | Register | Unit | R/W |
|--------|-------------|----------|------|-----|
| DHW Tank temperature 1 | DHW tank temperature sensor 1 | 11264 | °C | R |
| DHW Tank temperature 2 | DHW tank temperature sensor 2 | 11266 | °C | R |
| DHW Charging time limit | Maximum charging time | 11280 | min | R/W |
| DHW Flow setpoint boost | Flow temperature boost (Vorlaufsollwertüberhöhung) | 11290 | °C | R/W |
| DHW Switching differential | Switching differential (Schaltdifferenz) | 11294 | °C | R/W |
| DHW Max charging temperature | Maximum charging temperature | 11299 | °C | R/W |
| DHW Pump speed | DHW pump speed (Trinkwasserpumpe) | 11373 | % | R |
| DHW Intermediate circuit pump speed | Intermediate circuit pump speed | 11375 | % | R |
| DHW Current setpoint | Current active DHW setpoint | 11379 | °C | R |
| DHW Circulation temperature | Circulation temperature | 11381 | °C | R |
| DHW Charging temperature | Charging temperature (Ladetemperatur) | 11383 | °C | R |

### Binary Sensors

| Entity | Description | Register | Values |
|--------|-------------|----------|--------|
| DHW Pump | DHW pump state (Trinkwasserpumpe) | 11369 | 0=Off, 1=On |
| DHW Circulation pump | Circulation pump Q4 state | 11395 | 0=Off, 1=On |
| DHW Intermediate pump | Intermediate circuit pump Q33 state | 11411 | 0=Off, 1=On |

## Buffer Storage Tank (Pufferspeicher)

### Sensors

| Entity | Description | Register | Unit | R/W |
|--------|-------------|----------|------|-----|
| Buffer temperature 1 | Buffer tank temperature sensor 1 (B4) | 17410 | °C | R |
| Buffer temperature 2 | Buffer tank temperature sensor 2 (B41) | 17412 | °C | R |
| Buffer temperature 3 | Buffer tank temperature sensor 3 (B42) | 17463 | °C | R |
| Buffer status | Buffer storage status code | 17465 | - | R |
| Buffer setpoint | Buffer storage setpoint | 17466 | °C | R |

### Binary Sensors

| Entity | Description | Register | Values |
|--------|-------------|----------|--------|
| Buffer generator valve | Generator blocking valve Y4 (Erzeugersperrventil) | 17458 | 0=Off, 1=On |
| Buffer return valve | Buffer return valve Y15 | 17468 | 0=Off, 1=On |

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

- Boiler (Kessel) sensors
- Heatpump specific sensors (compressor, outdoor unit)
- Additional heating circuits (HC2, HC3)
- Error codes and diagnostics
