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

## Boiler (Kessel)

### Sensors

| Entity | Description | Register | Unit | R/W |
|--------|-------------|----------|------|-----|
| Boiler manual setpoint | Manual operation setpoint (Sollwert Handbetrieb) | 24576 | °C | R/W |
| Boiler nominal temp lift | Nominal temperature lift (Temperaturhub Nenn) | 24577 | °C | R/W |
| Boiler nominal power | Nominal power (Leistung Nenn) | 24581 | kW | R/W |
| Boiler base stage power | Base stage power (Leistung Grundstufe) | 24582 | kW | R/W |
| Burner hours maintenance interval | Maintenance interval in hours | 24583 | h | R/W |
| Burner hours since maintenance | Hours since last maintenance | 24585 | h | R |
| Burner starts interval | Burner starts interval | 24586 | - | R/W |
| Burner starts since maintenance | Starts since last maintenance | 24588 | - | R |
| Fan speed service threshold | Fan speed threshold for service message | 24589 | 1/min | R/W |
| Boiler status | Boiler status code | 24592 | - | R |
| Burner status | Burner status code | 24593 | - | R |
| Boiler pump speed | Boiler pump speed (Drehzahl Kesselpumpe) | 24596 | % | R |
| Boiler temperature | Current boiler temperature (Kesseltemperatur) | 24600 | °C | R |
| Boiler setpoint | Current boiler setpoint (Kesselsollwert) | 24604 | °C | R |
| Boiler return temperature | Return temperature (Kesselrücklauftemperatur) | 24608 | °C | R |
| Boiler fan speed | Current fan speed (Gebläsedrehzahl) | 24612 | 1/min | R |
| Boiler fan setpoint | Fan setpoint (Brennergebläsesollwert) | 24613 | 1/min | R |
| Boiler fan control | Current fan control (Aktuelle Gebläseansteuerung) | 24614 | % | R |
| Boiler relative power | Relative power (Relative Leistung) | 24616 | % | R |
| Ionization current | Ionization current (Ionisationsstrom) | 24618 | µA | R |
| Operating hours stage 1 | Operating hours stage 1 (Betriebsstunden 1. Stufe) | 24620 | h | R/W |
| Start counter stage 1 | Start counter stage 1 (Startzähler 1. Stufe) | 24621 | - | R/W |
| Operating hours heating | Operating hours heating mode | 24623 | h | R/W |
| Operating hours DHW | Operating hours DHW mode | 24625 | h | R/W |
| Total gas energy heating | Total gas energy for heating | 24629 | kWh | R/W |
| Total gas energy DHW | Total gas energy for DHW | 24631 | kWh | R/W |
| Total gas energy | Total gas energy | 24633 | kWh | R/W |
| Gas energy heating | Gas energy for heating | 24635 | kWh | R/W |
| Gas energy DHW | Gas energy for DHW | 24637 | kWh | R/W |
| Gas energy | Gas energy | 24639 | kWh | R |
| Firing automaton phase | Current firing automaton phase (1-21) | 24641 | - | R |

### Binary Sensors

| Entity | Description | Register | Values |
|--------|-------------|----------|--------|
| Ion current message | Ion current message (Meldung Ion Strom) | 24591 | 0=Off, 1=On |
| Boiler pump Q1 | Boiler pump state (Kesselpumpe Q1) | 24594 | 0=Off, 1=On |
| Generator lock | Generator lock via H-contact (Erzeugersperre) | 24644 | 0=Off, 1=On |

## General Functions (Allgemeine Funktionen)

### Sensors

| Entity | Description | Register | Unit | R/W |
|--------|-------------|----------|------|-----|
| Outdoor temperature | Outside air temperature (Außentemperatur) | 35851 | °C | R |
| Burner power mode | Burner power mode (1=Partial/2=Full/3=Max) | 35903 | - | R/W |
| Controller stop setpoint | Controller stop setpoint (Reglerstopp Sollwert) | 35906 | % | R/W |

### Binary Sensors

| Entity | Description | Register | Values |
|--------|-------------|----------|--------|
| Alarm relay status | Alarm relay state (Status Alarmrelais) | 35887 | 0=Off, 1=On |
| Chimney sweep function | Chimney sweep function (Schornsteinfegerfunktion) | 35901 | 0=Off, 1=On |
| Manual operation | Manual operation mode (Handbetrieb) | 35904 | 0=Off, 1=On |
| Controller stop function | Controller stop function (Reglerstoppfunktion) | 35905 | 0=Off, 1=On |

### Burner Power Modes (Brennerleistung)

| Value | German | English |
|-------|--------|---------|
| 1 | Teillast | Partial load |
| 2 | Volllast | Full load |
| 3 | Maximale Heizlast | Maximum heating load |

## Scale Factors

The following scale factors are used to convert raw register values:

| Factor | Value | Used for |
|--------|-------|----------|
| Temperature | 1/64 (0.015625) | All temperature values |
| Heating curve slope | 1/50 (0.02) | Heating curve steepness |
| Power | 1/10 (0.1) | Power in kW |
| Percent (scaled) | 1/100 (0.01) | Fan control %, ionization current |
| Hours | 1/3600 | Operating hours (stored as seconds) |

## Entity Naming

Entity IDs follow the pattern:
- Sensors: `sensor.broetje_heatpump_<entity_key>`
- Binary sensors: `binary_sensor.broetje_heatpump_<entity_key>`

Example: `sensor.broetje_heatpump_hc1_flow_temperature`

## IWR Entity Reference

For IWR/GTW-08 entities, see [`register_map.csv`](register_map.csv) for a comprehensive register map including all 885 registers with addresses, data types, descriptions (EN/DE), units, scaling factors, and categories.

## Future Entities

The following entities are planned for future versions:

- Additional heating circuits for ISR (HC2, HC3)
- Write support for R/W registers
