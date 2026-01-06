"""Constants for the Brötje Heatpump integration."""

from typing import Final

DOMAIN: Final = "broetje_heatpump"

# Default values
DEFAULT_PORT: Final = 502
DEFAULT_UNIT_ID: Final = 1
DEFAULT_SCAN_INTERVAL: Final = 30

# Configuration keys
CONF_UNIT_ID: Final = "unit_id"

# Manufacturer info
MANUFACTURER: Final = "Brötje"
DEFAULT_MODEL: Final = "Heatpump"

# Register types
REG_INPUT: Final = "input"
REG_HOLDING: Final = "holding"

# Scale factors from Brötje documentation
SCALE_TEMP: Final = 1 / 64  # 0.015625 - for temperature values
SCALE_CURVE: Final = 1 / 50  # 0.02 - for heating curve slope

# Operating mode enumeration (Betriebsart)
OPERATING_MODES: Final = {
    0: "protection",  # Schutzbetrieb
    1: "auto",        # Automatik
    2: "reduced",     # Reduziert
    3: "comfort",     # Komfort
}

# DHW Operating mode enumeration (Trinkwasser Betriebsart)
DHW_OPERATING_MODES: Final = {
    0: "off",   # Aus
    1: "on",    # Ein
    2: "eco",   # Eco
}

# DHW Release mode enumeration (Freigabe)
DHW_RELEASE_MODES: Final = {
    0: "24h",              # 24h/Tag
    1: "heating_program",  # Zeitprogramme Heizkreise
    2: "dhw_program",      # Zeitprogramm 4/TWW
}

# Legionella function mode enumeration
LEGIONELLA_MODES: Final = {
    0: "off",        # Aus
    1: "periodic",   # Periodisch
    2: "fixed_day",  # Fixer Wochentag
}

# Weekday enumeration
WEEKDAYS: Final = {
    1: "monday",
    2: "tuesday",
    3: "wednesday",
    4: "thursday",
    5: "friday",
    6: "saturday",
    7: "sunday",
}

# Modbus register map from Brötje documentation
# Heizkreis 1 (Heating Circuit 1)
REGISTER_MAP: Final = {
    # Operating mode - Register 1024
    "hc1_operating_mode": {
        "address": 1024,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Comfort setpoint - Register 1025
    "hc1_comfort_setpoint": {
        "address": 1025,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Reduced setpoint - Register 1026
    "hc1_reduced_setpoint": {
        "address": 1026,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Frost protection setpoint - Register 1027
    "hc1_frost_protection_setpoint": {
        "address": 1027,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Heating curve slope - Register 1028
    "hc1_heating_curve_slope": {
        "address": 1028,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_CURVE,
    },
    # Heating curve offset - Register 1029
    "hc1_heating_curve_offset": {
        "address": 1029,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "int16",
        "scale": SCALE_TEMP,
    },
    # Summer/Winter threshold - Register 1030
    "hc1_summer_winter_threshold": {
        "address": 1030,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Day heating threshold - Register 1032
    "hc1_day_heating_threshold": {
        "address": 1032,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "int16",
        "scale": SCALE_TEMP,
    },
    # Flow setpoint minimum - Register 1034
    "hc1_flow_setpoint_min": {
        "address": 1034,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Flow setpoint maximum - Register 1035
    "hc1_flow_setpoint_max": {
        "address": 1035,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Flow setpoint room thermostat - Register 1036
    "hc1_flow_setpoint_room_thermostat": {
        "address": 1036,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Room influence - Register 1038
    "hc1_room_influence": {
        "address": 1038,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Room temperature 1 - Register 1042 (read-only)
    "hc1_room_temperature": {
        "address": 1042,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Room setpoint 1 - Register 1044 (read-only)
    "hc1_room_setpoint": {
        "address": 1044,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Flow temperature 1 - Register 1046 (read-only)
    "hc1_flow_temperature": {
        "address": 1046,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Flow setpoint 1 - Register 1048 (read-only)
    "hc1_flow_setpoint": {
        "address": 1048,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Room thermostat demand - Register 1050 (read-only)
    "hc1_room_thermostat_demand": {
        "address": 1050,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Heating circuit status - Register 1054 (read-only)
    "hc1_status": {
        "address": 1054,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Heating circuit on/off - Register 1055
    "hc1_enabled": {
        "address": 1055,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Mixer boost - Register 1077
    "hc1_mixer_boost": {
        "address": 1077,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Heating circuit pump 1 - Register 1095 (read-only)
    "hc1_pump": {
        "address": 1095,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Mixer open - Register 1097 (read-only)
    "hc1_mixer_open": {
        "address": 1097,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Mixer close - Register 1099 (read-only)
    "hc1_mixer_close": {
        "address": 1099,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Pump speed - Register 1101 (read-only)
    "hc1_pump_speed": {
        "address": 1101,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Pump speed minimum - Register 1128
    "hc1_pump_speed_min": {
        "address": 1128,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Pump speed maximum - Register 1129
    "hc1_pump_speed_max": {
        "address": 1129,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    
    # ===== TRINKWASSER (DHW - Domestic Hot Water) =====
    
    # DHW Operating mode - Register 10240
    "dhw_operating_mode": {
        "address": 10240,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # DHW Setpoint - Register 10241
    "dhw_setpoint": {
        "address": 10241,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # DHW Reduced setpoint - Register 10242
    "dhw_reduced_setpoint": {
        "address": 10242,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # DHW Release mode - Register 10243
    "dhw_release_mode": {
        "address": 10243,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Legionella function mode - Register 10244
    "dhw_legionella_mode": {
        "address": 10244,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Legionella periodic interval (days) - Register 10245
    "dhw_legionella_interval": {
        "address": 10245,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Legionella weekday - Register 10246
    "dhw_legionella_weekday": {
        "address": 10246,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Legionella time (minutes from 00:00) - Register 10247
    "dhw_legionella_time": {
        "address": 10247,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Legionella setpoint - Register 10249
    "dhw_legionella_setpoint": {
        "address": 10249,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Legionella dwell time (minutes) - Register 10250
    "dhw_legionella_dwell_time": {
        "address": 10250,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Circulation setpoint - Register 10263
    "dhw_circulation_setpoint": {
        "address": 10263,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # DHW Status - Register 10273 (read-only)
    "dhw_status": {
        "address": 10273,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    
    # ===== TRINKWASSERSPEICHER (DHW Storage Tank) =====
    
    # DHW Temperature 1 - Register 11264 (read-only)
    "dhw_tank_temp_1": {
        "address": 11264,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # DHW Temperature 2 - Register 11266 (read-only)
    "dhw_tank_temp_2": {
        "address": 11266,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Charging time limit - Register 11280
    "dhw_charging_time_limit": {
        "address": 11280,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Flow setpoint boost - Register 11290
    "dhw_flow_setpoint_boost": {
        "address": 11290,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Switching differential - Register 11294
    "dhw_switching_differential": {
        "address": 11294,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Maximum charging temperature - Register 11299
    "dhw_charging_temp_max": {
        "address": 11299,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # DHW pump state - Register 11369 (read-only)
    "dhw_pump": {
        "address": 11369,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # DHW pump speed - Register 11373 (read-only)
    "dhw_pump_speed": {
        "address": 11373,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # DHW intermediate circuit pump speed - Register 11375 (read-only)
    "dhw_intermediate_pump_speed": {
        "address": 11375,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # DHW current setpoint - Register 11379 (read-only)
    "dhw_current_setpoint": {
        "address": 11379,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # DHW circulation temperature - Register 11381 (read-only)
    "dhw_circulation_temp": {
        "address": 11381,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # DHW charging temperature - Register 11383 (read-only)
    "dhw_charging_temp": {
        "address": 11383,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Circulation pump Q4 state - Register 11395 (read-only)
    "dhw_circulation_pump": {
        "address": 11395,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Intermediate circuit pump Q33 state - Register 11411 (read-only)
    "dhw_intermediate_pump": {
        "address": 11411,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    
    # ===== PUFFERSPEICHER (Buffer Storage Tank) =====
    
    # Buffer temperature 1 (B4) - Register 17410 (read-only)
    "buffer_temp_1": {
        "address": 17410,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Buffer temperature 2 (B41) - Register 17412 (read-only)
    "buffer_temp_2": {
        "address": 17412,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Generator blocking valve Y4 state - Register 17458 (read-only)
    "buffer_generator_valve": {
        "address": 17458,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Buffer temperature 3 (B42) - Register 17463 (read-only)
    "buffer_temp_3": {
        "address": 17463,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Buffer status - Register 17465 (read-only)
    "buffer_status": {
        "address": 17465,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Buffer setpoint - Register 17466 (read-only)
    "buffer_setpoint": {
        "address": 17466,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Buffer return valve Y15 state - Register 17468 (read-only)
    "buffer_return_valve": {
        "address": 17468,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
}

# Sensor definitions
SENSORS: Final = {
    "hc1_comfort_setpoint": {
        "register": "hc1_comfort_setpoint",
        "translation_key": "hc1_comfort_setpoint",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "hc1_reduced_setpoint": {
        "register": "hc1_reduced_setpoint",
        "translation_key": "hc1_reduced_setpoint",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "hc1_frost_protection_setpoint": {
        "register": "hc1_frost_protection_setpoint",
        "translation_key": "hc1_frost_protection_setpoint",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "hc1_heating_curve_slope": {
        "register": "hc1_heating_curve_slope",
        "translation_key": "hc1_heating_curve_slope",
        "device_class": None,
        "unit": None,
        "state_class": "measurement",
        "icon": "mdi:chart-line",
    },
    "hc1_heating_curve_offset": {
        "register": "hc1_heating_curve_offset",
        "translation_key": "hc1_heating_curve_offset",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "hc1_summer_winter_threshold": {
        "register": "hc1_summer_winter_threshold",
        "translation_key": "hc1_summer_winter_threshold",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "hc1_day_heating_threshold": {
        "register": "hc1_day_heating_threshold",
        "translation_key": "hc1_day_heating_threshold",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "hc1_flow_setpoint_min": {
        "register": "hc1_flow_setpoint_min",
        "translation_key": "hc1_flow_setpoint_min",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "hc1_operating_mode": {
        "register": "hc1_operating_mode",
        "translation_key": "hc1_operating_mode",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:thermostat",
    },
    "hc1_flow_setpoint_max": {
        "register": "hc1_flow_setpoint_max",
        "translation_key": "hc1_flow_setpoint_max",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "hc1_flow_setpoint_room_thermostat": {
        "register": "hc1_flow_setpoint_room_thermostat",
        "translation_key": "hc1_flow_setpoint_room_thermostat",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "hc1_room_influence": {
        "register": "hc1_room_influence",
        "translation_key": "hc1_room_influence",
        "device_class": None,
        "unit": "%",
        "state_class": "measurement",
        "icon": "mdi:home-thermometer",
    },
    "hc1_room_temperature": {
        "register": "hc1_room_temperature",
        "translation_key": "hc1_room_temperature",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "hc1_room_setpoint": {
        "register": "hc1_room_setpoint",
        "translation_key": "hc1_room_setpoint",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "hc1_flow_temperature": {
        "register": "hc1_flow_temperature",
        "translation_key": "hc1_flow_temperature",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "hc1_flow_setpoint": {
        "register": "hc1_flow_setpoint",
        "translation_key": "hc1_flow_setpoint",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "hc1_status": {
        "register": "hc1_status",
        "translation_key": "hc1_status",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:information-outline",
    },
    "hc1_mixer_boost": {
        "register": "hc1_mixer_boost",
        "translation_key": "hc1_mixer_boost",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "hc1_pump_speed": {
        "register": "hc1_pump_speed",
        "translation_key": "hc1_pump_speed",
        "device_class": None,
        "unit": "%",
        "state_class": "measurement",
        "icon": "mdi:pump",
    },
    "hc1_pump_speed_min": {
        "register": "hc1_pump_speed_min",
        "translation_key": "hc1_pump_speed_min",
        "device_class": None,
        "unit": "%",
        "state_class": "measurement",
        "icon": "mdi:pump",
    },
    "hc1_pump_speed_max": {
        "register": "hc1_pump_speed_max",
        "translation_key": "hc1_pump_speed_max",
        "device_class": None,
        "unit": "%",
        "state_class": "measurement",
        "icon": "mdi:pump",
    },
    
    # ===== DHW (Trinkwasser) Sensors =====
    
    "dhw_operating_mode": {
        "register": "dhw_operating_mode",
        "translation_key": "dhw_operating_mode",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:water-boiler",
        "enum_map": "dhw_operating_modes",
    },
    "dhw_setpoint": {
        "register": "dhw_setpoint",
        "translation_key": "dhw_setpoint",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "dhw_reduced_setpoint": {
        "register": "dhw_reduced_setpoint",
        "translation_key": "dhw_reduced_setpoint",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "dhw_release_mode": {
        "register": "dhw_release_mode",
        "translation_key": "dhw_release_mode",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:clock-outline",
        "enum_map": "dhw_release_modes",
    },
    "dhw_legionella_mode": {
        "register": "dhw_legionella_mode",
        "translation_key": "dhw_legionella_mode",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:bacteria",
        "enum_map": "legionella_modes",
    },
    "dhw_legionella_interval": {
        "register": "dhw_legionella_interval",
        "translation_key": "dhw_legionella_interval",
        "device_class": None,
        "unit": "d",
        "state_class": "measurement",
        "icon": "mdi:calendar-refresh",
    },
    "dhw_legionella_weekday": {
        "register": "dhw_legionella_weekday",
        "translation_key": "dhw_legionella_weekday",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:calendar-week",
        "enum_map": "weekdays",
    },
    "dhw_legionella_time": {
        "register": "dhw_legionella_time",
        "translation_key": "dhw_legionella_time",
        "device_class": None,
        "unit": "min",
        "state_class": None,
        "icon": "mdi:clock-outline",
    },
    "dhw_legionella_setpoint": {
        "register": "dhw_legionella_setpoint",
        "translation_key": "dhw_legionella_setpoint",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "dhw_legionella_dwell_time": {
        "register": "dhw_legionella_dwell_time",
        "translation_key": "dhw_legionella_dwell_time",
        "device_class": None,
        "unit": "min",
        "state_class": "measurement",
        "icon": "mdi:timer-outline",
    },
    "dhw_circulation_setpoint": {
        "register": "dhw_circulation_setpoint",
        "translation_key": "dhw_circulation_setpoint",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "dhw_status": {
        "register": "dhw_status",
        "translation_key": "dhw_status",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:information-outline",
    },
    
    # ===== DHW Storage Tank (Trinkwasserspeicher) Sensors =====
    
    "dhw_tank_temp_1": {
        "register": "dhw_tank_temp_1",
        "translation_key": "dhw_tank_temp_1",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "dhw_tank_temp_2": {
        "register": "dhw_tank_temp_2",
        "translation_key": "dhw_tank_temp_2",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "dhw_charging_time_limit": {
        "register": "dhw_charging_time_limit",
        "translation_key": "dhw_charging_time_limit",
        "device_class": None,
        "unit": "min",
        "state_class": "measurement",
        "icon": "mdi:timer-outline",
    },
    "dhw_flow_setpoint_boost": {
        "register": "dhw_flow_setpoint_boost",
        "translation_key": "dhw_flow_setpoint_boost",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "dhw_switching_differential": {
        "register": "dhw_switching_differential",
        "translation_key": "dhw_switching_differential",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "dhw_charging_temp_max": {
        "register": "dhw_charging_temp_max",
        "translation_key": "dhw_charging_temp_max",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "dhw_pump_speed": {
        "register": "dhw_pump_speed",
        "translation_key": "dhw_pump_speed",
        "device_class": None,
        "unit": "%",
        "state_class": "measurement",
        "icon": "mdi:pump",
    },
    "dhw_intermediate_pump_speed": {
        "register": "dhw_intermediate_pump_speed",
        "translation_key": "dhw_intermediate_pump_speed",
        "device_class": None,
        "unit": "%",
        "state_class": "measurement",
        "icon": "mdi:pump",
    },
    "dhw_current_setpoint": {
        "register": "dhw_current_setpoint",
        "translation_key": "dhw_current_setpoint",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "dhw_circulation_temp": {
        "register": "dhw_circulation_temp",
        "translation_key": "dhw_circulation_temp",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "dhw_charging_temp": {
        "register": "dhw_charging_temp",
        "translation_key": "dhw_charging_temp",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    
    # ===== Buffer Storage Tank (Pufferspeicher) Sensors =====
    
    "buffer_temp_1": {
        "register": "buffer_temp_1",
        "translation_key": "buffer_temp_1",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "buffer_temp_2": {
        "register": "buffer_temp_2",
        "translation_key": "buffer_temp_2",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "buffer_temp_3": {
        "register": "buffer_temp_3",
        "translation_key": "buffer_temp_3",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "buffer_status": {
        "register": "buffer_status",
        "translation_key": "buffer_status",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:information-outline",
    },
    "buffer_setpoint": {
        "register": "buffer_setpoint",
        "translation_key": "buffer_setpoint",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
}

# Binary sensor definitions
BINARY_SENSORS: Final = {
    "hc1_room_thermostat_demand": {
        "register": "hc1_room_thermostat_demand",
        "translation_key": "hc1_room_thermostat_demand",
        "device_class": "heat",
    },
    "hc1_enabled": {
        "register": "hc1_enabled",
        "translation_key": "hc1_enabled",
        "device_class": "running",
    },
    "hc1_pump": {
        "register": "hc1_pump",
        "translation_key": "hc1_pump",
        "device_class": "running",
    },
    "hc1_mixer_open": {
        "register": "hc1_mixer_open",
        "translation_key": "hc1_mixer_open",
        "device_class": None,
        "icon": "mdi:valve-open",
    },
    "hc1_mixer_close": {
        "register": "hc1_mixer_close",
        "translation_key": "hc1_mixer_close",
        "device_class": None,
        "icon": "mdi:valve-closed",
    },
    
    # ===== DHW Storage Tank (Trinkwasserspeicher) Binary Sensors =====
    
    "dhw_pump": {
        "register": "dhw_pump",
        "translation_key": "dhw_pump",
        "device_class": "running",
    },
    "dhw_circulation_pump": {
        "register": "dhw_circulation_pump",
        "translation_key": "dhw_circulation_pump",
        "device_class": "running",
    },
    "dhw_intermediate_pump": {
        "register": "dhw_intermediate_pump",
        "translation_key": "dhw_intermediate_pump",
        "device_class": "running",
    },
    
    # ===== Buffer Storage Tank (Pufferspeicher) Binary Sensors =====
    
    "buffer_generator_valve": {
        "register": "buffer_generator_valve",
        "translation_key": "buffer_generator_valve",
        "device_class": None,
        "icon": "mdi:valve",
    },
    "buffer_return_valve": {
        "register": "buffer_return_valve",
        "translation_key": "buffer_return_valve",
        "device_class": None,
        "icon": "mdi:valve",
    },
}
