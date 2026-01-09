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
SCALE_POWER: Final = 1 / 10  # 0.1 - for power in kW
SCALE_PERCENT_100: Final = 1 / 100  # 0.01 - for percentages scaled by 100
SCALE_HOURS: Final = 1 / 3600  # for hours stored as seconds

# Operating mode enumeration (Betriebsart)
OPERATING_MODES: Final = {
    0: "protection",  # Schutzbetrieb
    1: "auto",  # Automatik
    2: "reduced",  # Reduziert
    3: "comfort",  # Komfort
}

# DHW Operating mode enumeration (Trinkwasser Betriebsart)
DHW_OPERATING_MODES: Final = {
    0: "off",  # Aus
    1: "on",  # Ein
    2: "eco",  # Eco
}

# DHW Release mode enumeration (Freigabe)
DHW_RELEASE_MODES: Final = {
    0: "24h",  # 24h/Tag
    1: "heating_program",  # Zeitprogramme Heizkreise
    2: "dhw_program",  # Zeitprogramm 4/TWW
}

# Legionella function mode enumeration
LEGIONELLA_MODES: Final = {
    0: "off",  # Aus
    1: "periodic",  # Periodisch
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

# Burner power enumeration (Brennerleistung)
BURNER_POWER_MODES: Final = {
    1: "partial_load",  # Teillast
    2: "full_load",  # Volllast
    3: "max_heating_load",  # Maximale Heizlast
}

# Status codes (Statuscodes) - used by HC1 Status, Buffer Status, etc.
# From Brötje documentation Table 5 "Status codes (2 byte value)"
STATUS_CODES: Final = {
    0: "unknown",
    1: "slt_tripped",  # STB angesprochen
    2: "fault",  # Störung
    3: "limiter_tripped",  # Wächter angesprochen
    4: "manual_control",  # Handbetrieb aktiv
    5: "chimney_sweep_high",  # Schornsteinfegerfkt, Volllast
    6: "chimney_sweep_low",  # Schornsteinfegerfkt, Teillast
    7: "chimney_sweep_active",  # Schornsteinfegerfkt aktiv
    8: "locked_manual",  # Gesperrt, manuell
    9: "locked_automatic",  # Gesperrt, automatisch
    10: "locked",  # Gesperrt
    11: "protective_start",  # Anfahrentlastung
    12: "protective_start_low",  # Anfahrentlastung, Teillast
    13: "return_limitation",  # Rücklaufbegrenzung
    14: "return_limitation_low",  # Rücklaufbegrenzung, Teillast
    15: "released",  # Freigegeben
    16: "released_low",  # Freigegeben, Teillast
    17: "overrun_active",  # Nachlauf aktiv
    18: "in_operation",  # In Betrieb
    19: "released_2",  # Freigegeben
    20: "min_limitation",  # Minimalbegrenzung
    21: "min_limitation_low",  # Minimalbegrenzung, Teillast
    22: "min_limitation_active",  # Minimalbegrenzung aktiv
    23: "frost_prot_plant",  # Anlagefrostschutz aktiv
    24: "frost_protection",  # Frostschutz aktiv
    25: "off",  # Aus
    26: "emergency_operation",  # Notbetrieb
    27: "locked_externally",  # Gesperrt, extern
    51: "no_request",  # Keine Anforderung
    52: "frost_prot_collector",  # Kollektorfrostschutz aktiv
    53: "recooling_active",  # Rückkühlung aktiv
    54: "max_tank_temp",  # Max Speichertemp erreicht
    55: "evaporation_prot",  # Verdampfungsschutz aktiv
    56: "overtemp_prot",  # Überhitzschutz aktiv
    57: "max_charging_temp",  # Max Ladetemp erreicht
    58: "charging_dhw",  # Ladung Trinkwasser
    59: "charging_buffer",  # Ladung Pufferspeicher
    60: "charging_pool",  # Ladung Schwimmbad
    61: "min_charge_temp_not_reached",  # Min Ladetemp nicht erreicht
    62: "temp_diff_insufficient",  # Temp'differenz ungenügend
    63: "radiation_insufficient",  # Einstrahlung ungenügend
    67: "forced_charging",  # Zwangsladung aktiv
    68: "partial_charging",  # Teilladung aktiv
    69: "charging_active",  # Ladung aktiv
    70: "charged_max_tank",  # Geladen, max Speichertemp
    71: "charged_max_charging",  # Geladen, max Ladetemp
    72: "charged_forced",  # Geladen, Zwanglad Solltemp
    73: "charged_required",  # Teilgeladen, Solltemperatur
    74: "part_charged_required",  # Teilgeladen, Solltemperatur
    75: "charged",  # Geladen
    76: "cold",  # Kalt
    77: "recooling_collector",  # Rückkühlung via Kollektor
    78: "recooling_heat_gen",  # Rückkühlung via Erz/Hk's
    79: "discharging_prot",  # Entladeschutz aktiv
    80: "charge_time_limit",  # Ladezeitbegrenzung aktiv
    81: "charging_locked",  # Ladung gesperrt
    82: "charging_lock_active",  # Ladesperre aktiv
    83: "forced_max_tank",  # Zwang, max Speichertemp
    84: "forced_max_charging",  # Zwang, max Ladetemperatur
    85: "forced_legionella",  # Zwang, Legionellensollwert
    86: "forced_nominal",  # Zwang, Nennsollwert
    87: "el_charging_legionella",  # Ladung Elektro, Leg'sollwert
    88: "el_charging_nominal",  # Ladung Elektro, Nennsollwert
    89: "el_charging_reduced",  # Ladung Elektro, Red'sollwert
    90: "el_charging_frost",  # Ladung Elektro, Fros'sollwert
    91: "el_heater_released",  # Elektroeinsatz freigegeben
    92: "push_legionella",  # Push, Legionellensollwert
    93: "push_nominal",  # Push, Nennsollwert
    94: "push_active",  # Push aktiv
    95: "charging_legionella",  # Ladung, Legionellensollwert
    96: "charging_nominal",  # Ladung, Nennsollwert
    97: "charging_reduced",  # Ladung, Reduziertsollwert
    98: "charged_legionella",  # Geladen, Legio'temperatur
    99: "charged_nominal_temp",  # Geladen, Nenntemperatur
    100: "charged_reduced_temp",  # Geladen, Reduz'temperatur
    101: "frost_prot_room",  # Raumfrostschutz aktiv
    102: "floor_curing",  # Estrichfunktion aktiv
    103: "restricted_boiler",  # Eingeschränkt, Kesselschutz
    104: "restricted_dhw",  # Eingeschränkt, TWW-Vorrang
    105: "restricted_buffer",  # Eingeschränkt, Puffer
    106: "heating_restricted",  # Heizbetrieb eingeschränkt
    107: "forced_draw_buffer",  # Zwangsabnahme Puffer
    108: "forced_draw_dhw",  # Zwangsabnahme TWW
    109: "forced_draw_source",  # Zwangsabnahme Erzeuger
    110: "forced_draw",  # Zwangsabnahme
    111: "opt_start_boost",  # Einschaltopt+Schnellaufheiz
    112: "optimum_start",  # Einschaltoptimierung
    113: "boost_heating",  # Schnellaufheizung
    114: "comfort_heating",  # Heizbetrieb Komfort
    115: "optimum_stop",  # Ausschaltoptimierung
    116: "reduced_heating",  # Heizbetrieb Reduziert
    117: "frost_prot_flow",  # Vorlauffrostschutz aktiv
    118: "summer_operation",  # Sommerbetrieb
    119: "eco_24h",  # Tages-Eco aktiv
    120: "setback_reduced",  # Absenkung Reduziert
    121: "setback_frost",  # Absenkung Frostschutz
    122: "room_temp_limit",  # Raumtemp'begrenzung
    124: "charging_restricted",  # Ladung eingeschränkt
    137: "heating_mode",  # Heizbetrieb
    141: "boiler_frost_prot",  # Kesselfrostschutz aktiv
    142: "recooling_dhw_hc",  # Rückkühlung via TWW/Hk's
    143: "charged_min_temp",  # Geladen, Min Ladetemp
    147: "hot",  # Warm
    151: "charging_dhw_buffer_pool",  # Lad'ng TWW+Puffer+Sch'bad
    152: "charging_dhw_buffer",  # Ladung Trinkwasser+Puffer
    153: "charging_dhw_pool",  # Ladung Trinkwasser+Sch'bad
    154: "charging_buffer_pool",  # Ladung Puffer+Schwimmbad
    155: "heating_mode_source",  # Heizbetrieb Erzeuger
    156: "heated_max_pool",  # Geheizt, max Schw'badtemp
    157: "heated_setpoint_source",  # Geheizt, Sollwert Erzeuger
    158: "heated_setpoint_solar",  # Geheizt, Sollwert Solar
    159: "heated",  # Geheizt
    160: "heating_solar_off",  # Heizbetrieb Solar Aus
    161: "heating_source_off",  # Heizbetrieb Erzeuger Aus
    162: "heating_off",  # Heizbetrieb Aus
    166: "operation_hc",  # In Betrieb für Heizkreis
    167: "part_load_hc",  # In Teillastbetrieb für HK
    168: "operation_dhw",  # In Betrieb für Trinkwasser
    169: "part_load_dhw",  # In Teillastbetrieb für TWW
    170: "operation_hc_dhw",  # In Betrieb für HK, TWW
    171: "part_load_hc_dhw",  # In Teillastbetrieb für HK.TWW
    172: "locked_solid_fuel",  # Gesperrt, Feststoffkessel
    173: "released_hc_dhw",  # Freigegeben für HK, TWW
    174: "released_dhw",  # Freigegeben für TWW
    175: "released_hc",  # Freigegeben für HK
    176: "locked_outside_temp",  # Gesperrt, Aussentemperatur
    197: "electric_on",  # Elektro Ein
    198: "locked_economy",  # Gesperrt, Ökobetrieb
    199: "consumption",  # Zapfbetrieb
    200: "ready",  # Bereit
    203: "full_charging",  # Durchladung aktiv
    204: "locked_heating",  # Gesperrt, Heizbetrieb
    205: "locked_source",  # Gesperrt, Erzeuger
    206: "locked_buffer",  # Gesperrt, Puffer
    207: "comp_runtime_min",  # Verd'laufzeit Min aktiv, Kühl
    211: "lockout_position",  # Störstellung
    212: "start_prevention",  # Startverhinderung
    213: "shutdown",  # Ausserbetriebsetzung
    214: "safety_time",  # Sicherheitszeit
    215: "startup",  # Inbetriebsetzung
    216: "standby",  # Standby
    217: "home_run",  # Heimlauf
    218: "prepurge",  # Vorlüften
    219: "postpurge",  # Nachlüften
    220: "controller_stop",  # Reglerstopp aktiv
    221: "keep_hot_on",  # Warmhaltebetrieb ein
    222: "keep_hot_active",  # Warmhaltebetrieb aktiv
    223: "frost_prot_instant",  # Frostschutz Durchl'erhitzer
    224: "ignition",  # Zünden
    225: "settling_time",  # Einschwingzeit
    226: "exotic_gas",  # Exotengasbetrieb
    227: "drift_test",  # Drifttest aktiv
    228: "special_operation",  # Sonderbetrieb
    231: "start_drift_test",  # Start manueller Drifttest
    232: "flue_gas_switchoff",  # Abgastemp, Abschaltung
    233: "flue_gas_output_red",  # Abgastemp, Leist'begrenzung
    234: "flue_gas_too_high",  # Abgastemperatur zu hoch
    235: "water_pressure_low",  # Wasserdruck zu niedrig
    236: "party_function",  # Partyfunktion aktiv
    237: "transfer_legionella",  # Umladung, Legionellensollwert
    238: "transfer_nominal",  # Umladung, Nennsollwert
    239: "transfer_reduced",  # Umladung, Reduziertsollwert
    240: "transfer_active",  # Umladung aktiv
    241: "residual_heat",  # Restwärmenutzung
    242: "restratification",  # Umschichtung aktiv
    243: "keep_hot_released",  # Warmhaltebetrieb freigegeb'
    244: "source_released",  # Erzeuger freigegeben
    245: "slt_limits_output",  # STB begrenzt Leistung
    246: "mains_undervoltage",  # Netzunterspannung
    247: "temp_drop_prot",  # Unterkühlschutz aktiv
    248: "continuous_pump",  # Pumpendauerlauf
    298: "warmer_function",  # Wärmerfunktion aktiv
    299: "cooler_function",  # Kälterfunktion aktiv
    300: "adverse_wind",  # Gegenwindfunktion aktiv
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
    # ===== KESSEL (Boiler) =====
    # Manual setpoint - Register 24576
    "boiler_manual_setpoint": {
        "address": 24576,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Nominal temperature lift - Register 24577
    "boiler_temp_lift_nominal": {
        "address": 24577,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Nominal power - Register 24581
    "boiler_power_nominal": {
        "address": 24581,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_POWER,
    },
    # Base stage power - Register 24582
    "boiler_power_base": {
        "address": 24582,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_POWER,
    },
    # Burner hours maintenance interval - Register 24583
    "boiler_burner_hours_interval": {
        "address": 24583,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Burner hours since maintenance - Register 24585
    "boiler_burner_hours_since_maint": {
        "address": 24585,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Burner starts interval - Register 24586
    "boiler_burner_starts_interval": {
        "address": 24586,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Burner starts since maintenance - Register 24588
    "boiler_burner_starts_since_maint": {
        "address": 24588,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Fan speed threshold for service - Register 24589
    "boiler_fan_speed_service_threshold": {
        "address": 24589,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Ion current message - Register 24591 (binary)
    "boiler_ion_message": {
        "address": 24591,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Boiler status - Register 24592 (read-only)
    "boiler_status": {
        "address": 24592,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Burner status - Register 24593 (read-only)
    "boiler_burner_status": {
        "address": 24593,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Boiler pump Q1 - Register 24594 (read-only)
    "boiler_pump": {
        "address": 24594,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Boiler pump speed - Register 24596 (read-only)
    "boiler_pump_speed": {
        "address": 24596,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Boiler temperature - Register 24600 (read-only)
    "boiler_temperature": {
        "address": 24600,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Boiler setpoint - Register 24604 (read-only)
    "boiler_setpoint": {
        "address": 24604,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Boiler return temperature - Register 24608 (read-only)
    "boiler_return_temp": {
        "address": 24608,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_TEMP,
    },
    # Fan speed - Register 24612 (read-only)
    "boiler_fan_speed": {
        "address": 24612,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Burner fan setpoint - Register 24613 (read-only)
    "boiler_fan_setpoint": {
        "address": 24613,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Current fan control - Register 24614 (read-only)
    "boiler_fan_control": {
        "address": 24614,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_PERCENT_100,
    },
    # Relative power - Register 24616 (read-only)
    "boiler_power_relative": {
        "address": 24616,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Ionization current - Register 24618 (read-only)
    "boiler_ionization_current": {
        "address": 24618,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": SCALE_PERCENT_100,
    },
    # Operating hours stage 1 - Register 24620
    "boiler_operating_hours_stage1": {
        "address": 24620,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Start counter stage 1 - Register 24621 (uint32, 2 registers)
    "boiler_start_count_stage1": {
        "address": 24621,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    # Operating hours heating - Register 24623 (uint32, 2 registers)
    "boiler_operating_hours_heating": {
        "address": 24623,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": SCALE_HOURS,
    },
    # Operating hours DHW - Register 24625 (uint32, 2 registers)
    "boiler_operating_hours_dhw": {
        "address": 24625,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": SCALE_HOURS,
    },
    # Total gas energy heating - Register 24629 (uint32, 2 registers)
    "boiler_gas_energy_heating_total": {
        "address": 24629,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    # Total gas energy DHW - Register 24631 (uint32, 2 registers)
    "boiler_gas_energy_dhw_total": {
        "address": 24631,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    # Total gas energy - Register 24633 (uint32, 2 registers)
    "boiler_gas_energy_total": {
        "address": 24633,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    # Gas energy heating - Register 24635 (uint32, 2 registers)
    "boiler_gas_energy_heating": {
        "address": 24635,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    # Gas energy DHW - Register 24637 (uint32, 2 registers)
    "boiler_gas_energy_dhw": {
        "address": 24637,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    # Gas energy - Register 24639 (uint32, 2 registers)
    "boiler_gas_energy": {
        "address": 24639,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    # Firing automaton phase - Register 24641 (read-only)
    "boiler_firing_phase": {
        "address": 24641,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Generator lock via H-contact - Register 24644 (read-only)
    "boiler_generator_lock": {
        "address": 24644,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # ===== ALLGEMEINE FUNKTIONEN (General Functions) =====
    # Outdoor temperature - Register 35851 (read-only, signed)
    "outdoor_temperature": {
        "address": 35851,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "int16",
        "scale": SCALE_TEMP,
    },
    # Reset alarm relay - Register 35862
    "reset_alarm_relay": {
        "address": 35862,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Alarm relay status - Register 35887 (read-only)
    "alarm_relay_status": {
        "address": 35887,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Chimney sweep function - Register 35901
    "chimney_sweep_function": {
        "address": 35901,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Burner power mode - Register 35903
    "burner_power_mode": {
        "address": 35903,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Manual operation - Register 35904
    "manual_operation": {
        "address": 35904,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Controller stop function - Register 35905
    "controller_stop_function": {
        "address": 35905,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Controller stop setpoint - Register 35906
    "controller_stop_setpoint": {
        "address": 35906,
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
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:information-outline",
        "enum_map": "status_codes",
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
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:information-outline",
        "enum_map": "status_codes",
    },
    "buffer_setpoint": {
        "register": "buffer_setpoint",
        "translation_key": "buffer_setpoint",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    # ===== Boiler (Kessel) Sensors =====
    "boiler_manual_setpoint": {
        "register": "boiler_manual_setpoint",
        "translation_key": "boiler_manual_setpoint",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "boiler_temp_lift_nominal": {
        "register": "boiler_temp_lift_nominal",
        "translation_key": "boiler_temp_lift_nominal",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "boiler_power_nominal": {
        "register": "boiler_power_nominal",
        "translation_key": "boiler_power_nominal",
        "device_class": "power",
        "unit": "kW",
        "state_class": "measurement",
    },
    "boiler_power_base": {
        "register": "boiler_power_base",
        "translation_key": "boiler_power_base",
        "device_class": "power",
        "unit": "kW",
        "state_class": "measurement",
    },
    "boiler_burner_hours_interval": {
        "register": "boiler_burner_hours_interval",
        "translation_key": "boiler_burner_hours_interval",
        "device_class": "duration",
        "unit": "h",
        "state_class": "measurement",
        "icon": "mdi:clock-outline",
    },
    "boiler_burner_hours_since_maint": {
        "register": "boiler_burner_hours_since_maint",
        "translation_key": "boiler_burner_hours_since_maint",
        "device_class": "duration",
        "unit": "h",
        "state_class": "total_increasing",
        "icon": "mdi:clock-alert-outline",
    },
    "boiler_burner_starts_interval": {
        "register": "boiler_burner_starts_interval",
        "translation_key": "boiler_burner_starts_interval",
        "device_class": None,
        "unit": None,
        "state_class": "measurement",
        "icon": "mdi:counter",
    },
    "boiler_burner_starts_since_maint": {
        "register": "boiler_burner_starts_since_maint",
        "translation_key": "boiler_burner_starts_since_maint",
        "device_class": None,
        "unit": None,
        "state_class": "total_increasing",
        "icon": "mdi:counter",
    },
    "boiler_fan_speed_service_threshold": {
        "register": "boiler_fan_speed_service_threshold",
        "translation_key": "boiler_fan_speed_service_threshold",
        "device_class": None,
        "unit": "1/min",
        "state_class": "measurement",
        "icon": "mdi:fan",
    },
    "boiler_status": {
        "register": "boiler_status",
        "translation_key": "boiler_status",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:information-outline",
    },
    "boiler_burner_status": {
        "register": "boiler_burner_status",
        "translation_key": "boiler_burner_status",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:fire",
    },
    "boiler_pump_speed": {
        "register": "boiler_pump_speed",
        "translation_key": "boiler_pump_speed",
        "device_class": None,
        "unit": "%",
        "state_class": "measurement",
        "icon": "mdi:pump",
    },
    "boiler_temperature": {
        "register": "boiler_temperature",
        "translation_key": "boiler_temperature",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "boiler_setpoint": {
        "register": "boiler_setpoint",
        "translation_key": "boiler_setpoint",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "boiler_return_temp": {
        "register": "boiler_return_temp",
        "translation_key": "boiler_return_temp",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "boiler_fan_speed": {
        "register": "boiler_fan_speed",
        "translation_key": "boiler_fan_speed",
        "device_class": None,
        "unit": "1/min",
        "state_class": "measurement",
        "icon": "mdi:fan",
    },
    "boiler_fan_setpoint": {
        "register": "boiler_fan_setpoint",
        "translation_key": "boiler_fan_setpoint",
        "device_class": None,
        "unit": "1/min",
        "state_class": "measurement",
        "icon": "mdi:fan",
    },
    "boiler_fan_control": {
        "register": "boiler_fan_control",
        "translation_key": "boiler_fan_control",
        "device_class": None,
        "unit": "%",
        "state_class": "measurement",
        "icon": "mdi:fan",
    },
    "boiler_power_relative": {
        "register": "boiler_power_relative",
        "translation_key": "boiler_power_relative",
        "device_class": None,
        "unit": "%",
        "state_class": "measurement",
        "icon": "mdi:gauge",
    },
    "boiler_ionization_current": {
        "register": "boiler_ionization_current",
        "translation_key": "boiler_ionization_current",
        "device_class": None,
        "unit": "µA",
        "state_class": "measurement",
        "icon": "mdi:flash",
    },
    "boiler_operating_hours_stage1": {
        "register": "boiler_operating_hours_stage1",
        "translation_key": "boiler_operating_hours_stage1",
        "device_class": "duration",
        "unit": "h",
        "state_class": "total_increasing",
        "icon": "mdi:clock-outline",
    },
    "boiler_start_count_stage1": {
        "register": "boiler_start_count_stage1",
        "translation_key": "boiler_start_count_stage1",
        "device_class": None,
        "unit": None,
        "state_class": "total_increasing",
        "icon": "mdi:counter",
    },
    "boiler_operating_hours_heating": {
        "register": "boiler_operating_hours_heating",
        "translation_key": "boiler_operating_hours_heating",
        "device_class": "duration",
        "unit": "h",
        "state_class": "total_increasing",
        "icon": "mdi:clock-outline",
    },
    "boiler_operating_hours_dhw": {
        "register": "boiler_operating_hours_dhw",
        "translation_key": "boiler_operating_hours_dhw",
        "device_class": "duration",
        "unit": "h",
        "state_class": "total_increasing",
        "icon": "mdi:clock-outline",
    },
    "boiler_gas_energy_heating_total": {
        "register": "boiler_gas_energy_heating_total",
        "translation_key": "boiler_gas_energy_heating_total",
        "device_class": "energy",
        "unit": "kWh",
        "state_class": "total_increasing",
    },
    "boiler_gas_energy_dhw_total": {
        "register": "boiler_gas_energy_dhw_total",
        "translation_key": "boiler_gas_energy_dhw_total",
        "device_class": "energy",
        "unit": "kWh",
        "state_class": "total_increasing",
    },
    "boiler_gas_energy_total": {
        "register": "boiler_gas_energy_total",
        "translation_key": "boiler_gas_energy_total",
        "device_class": "energy",
        "unit": "kWh",
        "state_class": "total_increasing",
    },
    "boiler_gas_energy_heating": {
        "register": "boiler_gas_energy_heating",
        "translation_key": "boiler_gas_energy_heating",
        "device_class": "energy",
        "unit": "kWh",
        "state_class": "total_increasing",
    },
    "boiler_gas_energy_dhw": {
        "register": "boiler_gas_energy_dhw",
        "translation_key": "boiler_gas_energy_dhw",
        "device_class": "energy",
        "unit": "kWh",
        "state_class": "total_increasing",
    },
    "boiler_gas_energy": {
        "register": "boiler_gas_energy",
        "translation_key": "boiler_gas_energy",
        "device_class": "energy",
        "unit": "kWh",
        "state_class": "total_increasing",
    },
    "boiler_firing_phase": {
        "register": "boiler_firing_phase",
        "translation_key": "boiler_firing_phase",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:fire-circle",
    },
    # ===== General Functions (Allgemeine Funktionen) Sensors =====
    "outdoor_temperature": {
        "register": "outdoor_temperature",
        "translation_key": "outdoor_temperature",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "burner_power_mode": {
        "register": "burner_power_mode",
        "translation_key": "burner_power_mode",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:fire",
        "enum_map": "burner_power_modes",
    },
    "controller_stop_setpoint": {
        "register": "controller_stop_setpoint",
        "translation_key": "controller_stop_setpoint",
        "device_class": None,
        "unit": "%",
        "state_class": "measurement",
        "icon": "mdi:gauge",
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
    # ===== Boiler (Kessel) Binary Sensors =====
    "boiler_ion_message": {
        "register": "boiler_ion_message",
        "translation_key": "boiler_ion_message",
        "device_class": "problem",
    },
    "boiler_pump": {
        "register": "boiler_pump",
        "translation_key": "boiler_pump",
        "device_class": "running",
    },
    "boiler_generator_lock": {
        "register": "boiler_generator_lock",
        "translation_key": "boiler_generator_lock",
        "device_class": None,
        "icon": "mdi:lock",
    },
    # ===== General Functions (Allgemeine Funktionen) Binary Sensors =====
    "alarm_relay_status": {
        "register": "alarm_relay_status",
        "translation_key": "alarm_relay_status",
        "device_class": "problem",
    },
    "chimney_sweep_function": {
        "register": "chimney_sweep_function",
        "translation_key": "chimney_sweep_function",
        "device_class": None,
        "icon": "mdi:broom",
    },
    "manual_operation": {
        "register": "manual_operation",
        "translation_key": "manual_operation",
        "device_class": None,
        "icon": "mdi:hand-back-right",
    },
    "controller_stop_function": {
        "register": "controller_stop_function",
        "translation_key": "controller_stop_function",
        "device_class": None,
        "icon": "mdi:stop-circle",
    },
}
