"""IWR/GTW-08 device register, sensor, and enum definitions.

Based on GTW-08 Modbus Specification (7854678 - v.01 - 15092023).
"""

from __future__ import annotations

from typing import Any, Final

from ..const import REG_HOLDING

ZONE_ADDR_OFFSET: Final = 512
ZONE_TYPE_BASE_ADDR: Final = 640
ZONE_FUNCTION_BASE_ADDR: Final = 641

# Entity classification: (entity_category, entity_registry_enabled_default)
#   entity_category: None = primary, "diagnostic" = diagnostic
#   entity_registry_enabled_default: True = enabled, False = disabled by default
# Keys not listed default to (None, True).

IWR_STATIC_ENTITY_CLASSIFICATION: Final[dict[str, tuple[str | None, bool]]] = {
    # ===== Appliance core measurements — Primary =====
    "flow_temperature": (None, True),
    "return_temperature": (None, True),
    "outside_temperature": (None, True),
    "water_pressure": (None, True),
    "actual_power": (None, True),
    "cop": (None, True),
    "system_power": (None, True),
    "relative_power": (None, True),
    "pump_speed": (None, True),
    # ===== High-level status — Primary =====
    "main_status": (None, True),
    "sub_status": (None, True),
    "seasonal_mode": (None, True),
    "ch_enabled": (None, True),
    "dhw_enabled": (None, True),
    "cooling_enabled": (None, True),
    "service_notification": (None, True),
    # ===== Key binary status — Primary =====
    "status_heat_pump_on": (None, True),
    "status_flame_on": (None, True),
    "status_service_required": (None, True),
    "status_water_pressure_low": (None, True),
    "error_present": (None, True),
    "service_required": (None, True),
    "output_pump": (None, True),
    "output_dhw_active": (None, True),
    "output_ch_active": (None, True),
    "output_cooling_active": (None, True),
    # ===== Energy totals — Primary =====
    "total_energy_consumed": (None, True),
    "total_thermal_delivered": (None, True),
    "energy_consumed_ch": (None, True),
    "energy_consumed_dhw": (None, True),
    "thermal_delivered_ch": (None, True),
    "thermal_delivered_dhw": (None, True),
    "total_operating_hours": (None, True),
    "total_starts": (None, True),
    # ===== Appliance temperatures — Diagnostic, enabled =====
    "hp_flow_temperature": ("diagnostic", True),
    "hp_return_temperature": ("diagnostic", True),
    "exhaust_gas_temperature": ("diagnostic", True),
    "cu_flow_temperature": ("diagnostic", True),
    "cu_return_temperature": ("diagnostic", True),
    "cascade_flow_temperature": ("diagnostic", True),
    "cascade_return_temperature": ("diagnostic", True),
    "flow_rate": ("diagnostic", True),
    # ===== Setpoints and control — Diagnostic, enabled =====
    "ch_setpoint": ("diagnostic", True),
    "internal_dhw_setpoint": ("diagnostic", True),
    "dhw_flow_setpoint": ("diagnostic", True),
    "cooling_setpoint": ("diagnostic", True),
    "power_setpoint": ("diagnostic", True),
    "cooling_forced": ("diagnostic", True),
    # ===== Service counters — Diagnostic, enabled =====
    "hours_since_service": ("diagnostic", True),
    "hours_producing_since_service": ("diagnostic", True),
    "starts_since_service": ("diagnostic", True),
    # ===== Detailed energy breakdown — Diagnostic, enabled =====
    "energy_consumed_cooling": ("diagnostic", True),
    "energy_consumed_backup": ("diagnostic", True),
    "thermal_delivered_cooling": ("diagnostic", True),
    "energy_delivered_backup": ("diagnostic", True),
    "backup1_starts": ("diagnostic", True),
    "backup1_operating_hours": ("diagnostic", True),
    "backup2_starts": ("diagnostic", True),
    "backup2_operating_hours": ("diagnostic", True),
    "mains_power_hours": ("diagnostic", True),
    # ===== Appliance parameters — Diagnostic, disabled by default =====
    "summer_winter_threshold": ("diagnostic", False),
    "neutral_band": ("diagnostic", False),
    "frost_protection_threshold": ("diagnostic", False),
    "force_summer_mode": ("diagnostic", False),
    "control_power": ("diagnostic", False),
    "control_temperature": ("diagnostic", False),
    "control_algorithm_type": ("diagnostic", False),
    "control_heat_demand_type": ("diagnostic", False),
    "cop_threshold": ("diagnostic", False),
    "ionization_current": ("diagnostic", False),
    # ===== Status backup indicators — Diagnostic, disabled by default =====
    "status_backup1_on": ("diagnostic", False),
    "status_backup2_on": ("diagnostic", False),
    "status_dhw_backup_on": ("diagnostic", False),
    "status_power_down_needed": ("diagnostic", False),
    # ===== Bitfield internals — Diagnostic, disabled by default =====
    "demand_direct_zones": ("diagnostic", False),
    "demand_mixing_circuits": ("diagnostic", False),
    "demand_valves_open_safety": ("diagnostic", False),
    "demand_manual_heat": ("diagnostic", False),
    "demand_cooling_allowed": ("diagnostic", False),
    "demand_dhw_allowed": ("diagnostic", False),
    "demand_heat_engine_active": ("diagnostic", False),
    "output_3way_valve_open": ("diagnostic", False),
    "output_3way_valve": ("diagnostic", False),
    "output_3way_valve_closed": ("diagnostic", False),
    # ===== Discovery / system metadata — Diagnostic, disabled by default =====
    "gateway_device_type": ("diagnostic", False),
    "zone_count": ("diagnostic", False),
    "zones_disabled": ("diagnostic", False),
    "zones_ch": ("diagnostic", False),
    "zones_ch_cooling": ("diagnostic", False),
    "zones_dhw": ("diagnostic", False),
    "zones_process_heat": ("diagnostic", False),
    "zones_swimming_pool": ("diagnostic", False),
    "zones_others": ("diagnostic", False),
    "devices_connected": ("diagnostic", False),
    # ===== Board errors — Diagnostic, disabled by default =====
    "board1_error_code": ("diagnostic", False),
    "board1_error_severity": ("diagnostic", False),
    "board2_error_code": ("diagnostic", False),
    "board2_error_severity": ("diagnostic", False),
    "board3_error_code": ("diagnostic", False),
    "board3_error_severity": ("diagnostic", False),
    "board4_error_code": ("diagnostic", False),
    "board4_error_severity": ("diagnostic", False),
}

# Zone entity classification keyed by translation_key (zone-number-agnostic).
IWR_ZONE_ENTITY_CLASSIFICATION: Final[dict[str, tuple[str | None, bool]]] = {
    # ===== Zone essentials — Primary =====
    "zone_room_temp": (None, True),
    "zone_room_temp_measured": (None, True),
    "zone_flow_temp": (None, True),
    "zone_flow_setpoint": (None, True),
    "zone_room_setpoint": (None, True),
    "zone_heating_mode": (None, True),
    "zone_pump": (None, True),
    "zone_heat_demand": (None, True),
    "zone_activity": (None, True),
    "zone_operating_mode": (None, True),
    # ===== Zone energy/runtime — Primary =====
    "zone_pump_hours": (None, True),
    "zone_pump_starts": (None, True),
    # ===== Zone medium-advanced — Diagnostic, enabled =====
    "zone_outside_temp": ("diagnostic", True),
    "zone_time_program_selected": ("diagnostic", True),
    "zone_night_setback": ("diagnostic", True),
    "zone_heating_curve_gradient": ("diagnostic", True),
    "zone_heating_curve_footpoint": ("diagnostic", True),
    "zone_max_flow_setpoint": ("diagnostic", True),
    "zone_room_setpoint_manual": ("diagnostic", True),
    "zone_fixed_flow_setpoint": ("diagnostic", True),
    # ===== Zone commissioning metadata — Diagnostic, disabled by default =====
    "zone_function": ("diagnostic", False),
    "zone_device_type": ("diagnostic", False),
    "zone_type": ("diagnostic", False),
    "zone_control_mode": ("diagnostic", False),
    "zone_heating_control_strategy": ("diagnostic", False),
    # ===== Zone deep tuning — Diagnostic, disabled by default =====
    "zone_comfort_setpoint_1": ("diagnostic", False),
    "zone_comfort_setpoint_2": ("diagnostic", False),
    "zone_comfort_setpoint_3": ("diagnostic", False),
    "zone_comfort_setpoint_4": ("diagnostic", False),
    "zone_comfort_setpoint_5": ("diagnostic", False),
    "zone_cooling_room_setpoint_1": ("diagnostic", False),
    "zone_cooling_room_setpoint_2": ("diagnostic", False),
    "zone_cooling_room_setpoint_3": ("diagnostic", False),
    "zone_cooling_room_setpoint_4": ("diagnostic", False),
    "zone_cooling_room_setpoint_5": ("diagnostic", False),
    "zone_cooling_night_setback": ("diagnostic", False),
    "zone_holiday_setpoint": ("diagnostic", False),
    "zone_temporary_setpoint": ("diagnostic", False),
    "zone_dhw_comfort_setpoint": ("diagnostic", False),
    "zone_dhw_reduced_setpoint": ("diagnostic", False),
    "zone_dhw_holiday_setpoint": ("diagnostic", False),
    "zone_dhw_antilegionella_setpoint": ("diagnostic", False),
    "zone_swimming_pool_setpoint": ("diagnostic", False),
    "zone_process_heat_setpoint": ("diagnostic", False),
    "zone_cooling_mixing_setpoint": ("diagnostic", False),
    "zone_heating_curve_footpoint_night": ("diagnostic", False),
    "zone_max_preheat_time": ("diagnostic", False),
    "zone_mixing_valve_shift": ("diagnostic", False),
    "zone_mixing_valve_bandwidth": ("diagnostic", False),
    "zone_dhw_hysteresis": ("diagnostic", False),
    "zone_dhw_calorifier_offset": ("diagnostic", False),
    "zone_dhw_calorifier_raise": ("diagnostic", False),
    "zone_process_heat_hysteresis": ("diagnostic", False),
    "zone_process_heat_offset": ("diagnostic", False),
    "zone_process_heat_calorifier_raise": ("diagnostic", False),
    "zone_dhw_calorifier_hysteresis": ("diagnostic", False),
    "zone_pump_post_run": ("diagnostic", False),
    # ===== Zone low-level flags — Diagnostic, disabled by default =====
    "zone_flow_measurement": ("diagnostic", False),
    "zone_mixing_valve_opening": ("diagnostic", False),
    "zone_swimming_pool_pump": ("diagnostic", False),
    "zone_electrical_backup_output": ("diagnostic", False),
}

# Board discovery entities — all diagnostic, disabled by default.
IWR_BOARD_ENTITY_CLASSIFICATION: Final[tuple[str | None, bool]] = ("diagnostic", False)

# ===== IWR/GTW-08 Scale Factors =====
# These differ from ISR scale factors
IWR_SCALE_TEMP: Final = 0.01  # 0.01 °C resolution
IWR_SCALE_PRESSURE: Final = 0.1  # 0.1 bar resolution
IWR_SCALE_POWER: Final = 0.01  # 0.01 kW resolution
IWR_SCALE_COP: Final = 0.001  # COP resolution
IWR_SCALE_PUMP: Final = 0.1  # 0.1% pump speed
IWR_SCALE_ROOM_TEMP: Final = 0.1  # 0.1 °C for room temperature setpoints

# ===== IWR Enum Maps =====

# Tab.16 AM012 - Main appliance status
IWR_MAIN_STATUS: Final = {
    0: "standby",
    1: "heat_demand",
    2: "generator_start",
    3: "generator_ch",
    4: "generator_dhw",
    5: "generator_stop",
    6: "pump_post_run",
    7: "cooling_active",
    8: "controlled_stop",
    9: "blocking_mode",
    10: "locking_mode",
    11: "load_test_min",
    12: "load_test_ch_max",
    13: "load_test_dhw_max",
    15: "manual_heat_demand",
    16: "frost_protection",
    17: "deaeration",
    18: "control_unit_cooling",
    19: "reset_in_progress",
    20: "auto_filling",
    21: "halted",
    22: "forced_calibration",
    23: "factory_test",
    24: "hydronic_balancing",
    200: "device_mode",
    254: "unknown",
}

# Tab.17 AM014 - Sub status
IWR_SUB_STATUS: Final = {
    0: "standby",
    1: "anti_cycling",
    2: "close_hydraulic_valve",
    3: "close_pump",
    4: "waiting_for_start_cond",
    10: "close_ext_gas_valve",
    11: "start_to_glue_gas_valve",
    12: "close_flue_gas_valve",
    13: "fan_to_pre_purge",
    14: "wait_for_release_signal",
    15: "burner_on_command",
    16: "vps_test",
    17: "pre_ignition",
    18: "ignition",
    19: "flame_check",
    20: "interpurge",
    21: "generator_starting",
    30: "normal_int_setpoint",
    31: "limited_int_setpoint",
    32: "normal_power_control",
    33: "grad_level1_power_ctrl",
    34: "grad_level2_power_ctrl",
    35: "grad_level3_power_ctrl",
    36: "protect_flame_pwr_ctrl",
    37: "stabilization_time",
    38: "cold_start",
    39: "ch_resume",
    40: "su_remove_burner",
    41: "fan_to_post_purge",
    42: "open_ext_flue_gas_valve",
    43: "stop_fan_to_flue_gv_rpm",
    44: "stop_fan",
    45: "limited_pwr_on_tflue_gas",
    46: "auto_filling_install",
    47: "auto_filling_top_up",
    48: "reduced_set_point",
    49: "offset_adaption",
    60: "pump_post_running",
    61: "open_pump",
    62: "open_hydraulic_valve",
    63: "start_anticycle_time",
    65: "compressor_relieved",
    66: "hp_tmax_backup_on",
    67: "outdoor_limit_hp_off",
    68: "hp_stop_by_hybrid",
    69: "defrost_with_hp",
    70: "defrost_with_backup",
    71: "defrost_hp_backup",
    72: "source_pump_backup",
    73: "hp_flow_over_tmax",
    74: "source_pump_post_run",
    75: "hp_off_high_humidity",
    76: "hp_off_water_flow",
    78: "humidity_setpoint",
    79: "generators_relieved",
    80: "hp_relieved_cooling",
    81: "hp_stop_outdoor_temp",
    82: "hp_off_flow_tmax",
    83: "deair_pump_valve_ch",
    84: "deair_pump_valve_dhw",
    85: "deair_valve_ch",
    86: "deair_valve_dhw",
    88: "bl_backup_off",
    89: "bl_hp_off",
    90: "bl_hp_backup_off",
    91: "low_tariff",
    92: "pv_with_hp",
    93: "pv_hp_and_backup",
    94: "smart_grid",
    95: "waiting_for_waterpress",
    96: "no_producer_available",
    97: "increased_min_power",
    98: "decreased_max_power",
    102: "free_cool_pump_off",
    103: "free_cool_pump_on",
    104: "source_pump_pre_run",
    105: "calibration",
    106: "blocking_active",
    107: "warm_up",
    108: "defrost_curative",
    109: "defrost_preventive",
    200: "initialising_done",
    201: "initialising_csu",
    202: "init_identifiers",
    203: "init_bl_parameter",
    204: "init_safety_unit",
    205: "init_blocking",
    254: "state_unknown",
    255: "su_out_of_resets_wait",
}

# Seasonal mode (register 385)
IWR_SEASONAL_MODE: Final = {
    0: "winter",
    1: "frost_protection",
    2: "summer_neutral",
    3: "summer",
}

# Zone activity (CM130, register 1107 etc.)
IWR_ZONE_ACTIVITY: Final = {
    0: "off",
    1: "eco",
    2: "comfort",
    3: "anti_legionella",
}

# Zone operating mode (CM120, register 1108 etc.)
IWR_ZONE_OPERATING_MODE: Final = {
    0: "scheduling",
    1: "manual",
    2: "off",
    3: "temporary",
}

# Service notification type (register 513)
IWR_SERVICE_NOTIFICATION: Final = {
    0: "none",
    1: "a",
    2: "b",
    3: "c",
    4: "custom",
    5: "d",
}

# Error severity (registers 533, 535, etc.)
IWR_ERROR_SEVERITY: Final = {
    0: "locking",
    3: "blocking",
    6: "warning",
    255: "no_error",
}

# Zone function type (Tab.25/26, CP02X, registers 641 etc.)
IWR_ZONE_FUNCTION: Final = {
    0: "disable",
    1: "direct",
    2: "mixing_circuit",
    3: "swimming_pool",
    4: "high_temperature",
    5: "fan_convector",
    6: "dhw_tank",
    7: "electrical_dhw",
    8: "time_program",
    9: "process_heat",
    10: "dhw_layered",
    11: "dhw_internal_tank",
    12: "dhw_commercial_tank",
    13: "occupied",
    254: "dhw_primary",
}

# Device category lookup for 0xZZYY device type (Tab.26)
IWR_DEVICE_CATEGORY: Final = {
    0x00: "CU-GH",
    0x01: "CU-OH",
    0x02: "EHC",
    0x14: "MK",
    0x19: "SCB",
    0x1B: "EEC",
    0x1E: "Gateway",
}

# Zone control mode (CP32X, Tab.36/42, registers 649 etc.)
IWR_ZONE_CONTROL_MODE: Final = {
    0: "scheduling",
    1: "manual",
    2: "off",
}

# Tab.19 - Algorithm type (register 258)
IWR_ALGORITHM_TYPE: Final = {
    0: "remote_temp_and_power",
    1: "remote_power",
    2: "remote_temperature",
    3: "monitoring_only",
}

# Tab.20 - Heat demand type (register 259)
IWR_HEAT_DEMAND_TYPE: Final = {
    0: "standby",
    7: "heating",
    8: "cooling",
}

# Generic on/off enum (registers 389, 500, 501, 503)
IWR_ON_OFF: Final = {
    0: "off",
    1: "on",
}

# Zone current heating mode (register 1109 etc.)
IWR_ZONE_HEATING_MODE: Final = {
    0: "standby",
    1: "heating",
    2: "cooling",
}

# Zone type (register 640 etc.)
IWR_ZONE_TYPE: Final = {
    0: "not_present",
    1: "ch_only",
    2: "ch_and_cooling",
    3: "dhw",
    4: "process_heat",
    5: "swimming_pool",
    254: "other",
}

# Heating control strategy (register 671 etc.)
IWR_HEATING_CONTROL_STRATEGY: Final = {
    0: "auto",
    1: "room",
    2: "outdoor",
    3: "outdoor_and_room",
}

# Time program selection (register 688 etc.)
IWR_TIME_PROGRAM_SELECTED: Final = {
    0: "time_program_1",
    1: "time_program_2",
    2: "time_program_3",
}

# Cooling enabled mode (register 502)
IWR_COOLING_ENABLED: Final = {
    0: "off",
    1: "active_cooling",
    2: "free_cooling",
}

# Collected enum maps for IWR device
IWR_ENUM_MAPS: Final = {
    "iwr_main_status": IWR_MAIN_STATUS,
    "iwr_sub_status": IWR_SUB_STATUS,
    "iwr_seasonal_mode": IWR_SEASONAL_MODE,
    "iwr_zone_activity": IWR_ZONE_ACTIVITY,
    "iwr_zone_operating_mode": IWR_ZONE_OPERATING_MODE,
    "iwr_service_notification": IWR_SERVICE_NOTIFICATION,
    "iwr_error_severity": IWR_ERROR_SEVERITY,
    "iwr_algorithm_type": IWR_ALGORITHM_TYPE,
    "iwr_heat_demand_type": IWR_HEAT_DEMAND_TYPE,
    "iwr_zone_control_mode": IWR_ZONE_CONTROL_MODE,
    "iwr_zone_function": IWR_ZONE_FUNCTION,
    "iwr_on_off": IWR_ON_OFF,
    "iwr_cooling_enabled": IWR_COOLING_ENABLED,
    "iwr_zone_type": IWR_ZONE_TYPE,
    "iwr_zone_heating_mode": IWR_ZONE_HEATING_MODE,
    "iwr_heating_control_strategy": IWR_HEATING_CONTROL_STRATEGY,
    "iwr_time_program_selected": IWR_TIME_PROGRAM_SELECTED,
}

# ===== Zone Address Tables =====
# From Tab.33 and Tab.35 in the GTW-08 Modbus specification.
# Zones 1-12 addresses for each register type.

ZONE_ADDRESSES: Final = {
    # Tab.33 - Main zone registers (read-only)
    "CM040": [1100, 1612, 2124, 2636, 3148, 3660, 4172, 4684, 5196, 5708, 6220, 6732],
    "CM070": [1101, 1613, 2125, 2637, 3149, 3661, 4173, 4685, 5197, 5709, 6221, 6733],
    "CM190": [1102, 1614, 2126, 2638, 3150, 3662, 4174, 4686, 5198, 5710, 6222, 6734],
    "CM130": [1107, 1619, 2131, 2643, 3155, 3667, 5121, 5633, 6145, 6657, 7169, 7681],
    "CM120": [1108, 1620, 2132, 2644, 3156, 3668, 5122, 5634, 6146, 6658, 7170, 7682],
    "CM050": [1110, 1622, 2134, 2646, 3158, 3670, 5124, 5636, 6148, 6660, 7172, 7684],
    "CM010": [1111, 1623, 2135, 2647, 3159, 3671, 5125, 5637, 6149, 6661, 7173, 7685],
    # Tab.35 - Zone counter registers (read-only)
    "CC001": [1115, 1627, 2139, 2651, 3163, 3675, 4187, 4699, 5211, 5723, 6235, 6747],
    "CC010": [1117, 1629, 2141, 2652, 3165, 3677, 4189, 4771, 5213, 5725, 6237, 6749],
    # Tab.25 - Zone function type CP02X (R, base 641, +512/zone)
    "CP02X": [641, 1153, 1665, 2177, 2689, 3201, 3713, 4225, 4737, 5249, 5761, 6273],
    # Tab.25 - Zone device type (R, base 645, +512/zone)
    "DEV": [645, 1157, 1669, 2181, 2693, 3205, 3717, 4229, 4741, 5253, 5765, 6277],
    # Tab.36/42 - Zone control mode CP32X (R/W, base 649, +512/zone)
    "CP32X": [649, 1161, 1673, 2185, 2697, 3209, 3721, 4233, 4745, 5257, 5769, 6281],
    # Tab.37 - Zone fixed flow setpoint CP01X (R/W, base 648, +512/zone)
    "CP01X": [648, 1160, 1672, 2184, 2696, 3208, 3720, 4232, 4744, 5256, 5768, 6280],
    # Tab.43 - Zone room temp setpoint manual CP20X (R/W, base 664, +512/zone)
    "CP20X": [664, 1176, 1688, 2200, 2712, 3224, 3736, 4248, 4760, 5272, 5784, 6296],
    # Tab.39 - Heating curve gradient CP23X (R/W, base 674, +512/zone)
    "CP23X": [674, 1186, 1698, 2210, 2722, 3234, 3746, 4258, 4770, 5282, 5794, 6306],
    # Tab.40 - Heating curve footpoint CP21X (R/W, base 675, +512/zone)
    # NOTE: PDF has typos for Z5 (2722) and Z8 (4258); corrected to 2723/4259.
    "CP21X": [675, 1187, 1699, 2211, 2723, 3235, 3747, 4259, 4771, 5283, 5795, 6307],
}

# ===== Static Register Map (non-zone registers) =====

_IWR_STATIC_REGISTER_MAP: Final = {
    # --- Device Information GTW-08 (from German spec 7740782-01) ---
    "gateway_device_type": {
        "address": 11,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # --- Zone Detection (Tab.24) ---
    "zone_count": {
        "address": 189,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # --- Zone Count Subtypes (from German spec 7740782-01) ---
    "zones_disabled": {
        "address": 190,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "zones_ch": {
        "address": 191,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "zones_ch_cooling": {
        "address": 192,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "zones_dhw": {
        "address": 193,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "zones_process_heat": {
        "address": 194,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "zones_swimming_pool": {
        "address": 195,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "zones_others": {
        "address": 196,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # --- Temperature and Power Control (Tab.18) ---
    "control_power": {
        "address": 256,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "control_temperature": {
        "address": 257,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": IWR_SCALE_TEMP,
    },
    "control_algorithm_type": {
        "address": 258,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "control_heat_demand_type": {
        "address": 259,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # --- Main Appliance Information (Tab.12) ---
    "system_power": {
        "address": 272,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # --- Received Temperatures from CU (from German spec 7740782-01) ---
    "cu_flow_temperature": {
        "address": 273,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "int16",
        "scale": IWR_SCALE_TEMP,
    },
    "cu_return_temperature": {
        "address": 274,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "int16",
        "scale": IWR_SCALE_TEMP,
    },
    "error_list": {
        "address": 277,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "outside_temperature": {
        "address": 384,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "int16",
        "scale": IWR_SCALE_TEMP,
    },
    "seasonal_mode": {
        "address": 385,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # --- Appliance Parameters (from German spec 7740782-01) ---
    "summer_winter_threshold": {
        "address": 386,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": IWR_SCALE_TEMP,
    },
    "neutral_band": {
        "address": 387,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": IWR_SCALE_TEMP,
    },
    "frost_protection_threshold": {
        "address": 388,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "int16",
        "scale": IWR_SCALE_TEMP,
    },
    "force_summer_mode": {
        "address": 389,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "flow_temperature": {
        "address": 400,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "int16",
        "scale": IWR_SCALE_TEMP,
    },
    "return_temperature": {
        "address": 401,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "int16",
        "scale": IWR_SCALE_TEMP,
    },
    "exhaust_gas_temperature": {
        "address": 402,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "int16",
        "scale": IWR_SCALE_TEMP,
    },
    "hp_flow_temperature": {
        "address": 403,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "int16",
        "scale": IWR_SCALE_TEMP,
    },
    "hp_return_temperature": {
        "address": 404,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "int16",
        "scale": IWR_SCALE_TEMP,
    },
    # --- Internal Setpoints (from German spec 7740782-01) ---
    "internal_dhw_setpoint": {
        "address": 405,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": IWR_SCALE_TEMP,
    },
    "ch_setpoint": {
        "address": 406,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": IWR_SCALE_TEMP,
    },
    "cooling_setpoint": {
        "address": 407,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": IWR_SCALE_TEMP,
    },
    "dhw_flow_setpoint": {
        "address": 408,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": IWR_SCALE_TEMP,
    },
    "water_pressure": {
        "address": 409,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": IWR_SCALE_PRESSURE,
    },
    "flow_rate": {
        "address": 410,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": IWR_SCALE_TEMP,  # 0.01 l/min
    },
    "main_status": {
        "address": 411,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "sub_status": {
        "address": 412,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "relative_power": {
        "address": 413,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "power_setpoint": {
        "address": 414,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": IWR_SCALE_PUMP,  # 0.1%
    },
    "ionization_current": {
        "address": 415,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": IWR_SCALE_PRESSURE,  # 0.1 µA
    },
    "total_starts": {
        "address": 419,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    "total_operating_hours": {
        "address": 421,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    "backup1_starts": {
        "address": 423,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    "backup1_operating_hours": {
        "address": 425,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    "backup2_starts": {
        "address": 427,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    "backup2_operating_hours": {
        "address": 429,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    "mains_power_hours": {
        "address": 431,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    "energy_consumed_ch": {
        "address": 433,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    "energy_consumed_dhw": {
        "address": 435,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    "energy_consumed_cooling": {
        "address": 437,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    "total_energy_consumed": {
        "address": 439,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    "energy_consumed_backup": {
        "address": 441,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    "total_thermal_delivered": {
        "address": 443,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    "thermal_delivered_ch": {
        "address": 445,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    "thermal_delivered_dhw": {
        "address": 447,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    "thermal_delivered_cooling": {
        "address": 449,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    "energy_delivered_backup": {
        "address": 451,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    "pump_speed": {
        "address": 459,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": IWR_SCALE_PUMP,
    },
    "actual_power": {
        "address": 460,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": IWR_SCALE_POWER,
    },
    "cop": {
        "address": 9230,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": IWR_SCALE_COP,
    },
    "cop_threshold": {
        "address": 9231,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": IWR_SCALE_COP,
    },
    # --- Cascade Flow/Return Temperature (Tab.23) ---
    "cascade_flow_temperature": {
        "address": 7101,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "int16",
        "scale": IWR_SCALE_TEMP,
    },
    "cascade_return_temperature": {
        "address": 7163,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "int16",
        "scale": IWR_SCALE_TEMP,
    },
    # --- Bitfield registers (Tab.13-15) ---
    # Register 275 bits (Tab.13 - Heat demand bitfield)
    "demand_direct_zones": {
        "address": 275,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 0,
    },
    "demand_mixing_circuits": {
        "address": 275,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 1,
    },
    "demand_valves_open_safety": {
        "address": 275,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 2,
    },
    "demand_manual_heat": {
        "address": 275,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 3,
    },
    "demand_cooling_allowed": {
        "address": 275,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 4,
    },
    "demand_dhw_allowed": {
        "address": 275,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 5,
    },
    "demand_heat_engine_active": {
        "address": 275,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 6,
    },
    # Register 279 bits (Tab.14 - Output status 1)
    "status_flame_on": {
        "address": 279,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 0,
    },
    "status_heat_pump_on": {
        "address": 279,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 1,
    },
    "status_backup1_on": {
        "address": 279,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 2,
    },
    "status_backup2_on": {
        "address": 279,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 3,
    },
    "status_dhw_backup_on": {
        "address": 279,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 4,
    },
    "status_service_required": {
        "address": 279,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 5,
    },
    "status_power_down_needed": {
        "address": 279,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 6,
    },
    "status_water_pressure_low": {
        "address": 279,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 7,
    },
    # Register 280 bits (Tab.15 - Output status 2)
    "output_pump": {
        "address": 280,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 0,
    },
    "output_3way_valve_open": {
        "address": 280,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 1,
    },
    "output_3way_valve": {
        "address": 280,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 2,
    },
    "output_3way_valve_closed": {
        "address": 280,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 3,
    },
    "output_dhw_active": {
        "address": 280,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 4,
    },
    "output_ch_active": {
        "address": 280,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 5,
    },
    "output_cooling_active": {
        "address": 280,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "bool",
        "bit": 6,
    },
    # --- Appliance Enable/Disable (from German spec 7740782-01) ---
    "ch_enabled": {
        "address": 500,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "dhw_enabled": {
        "address": 501,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "cooling_enabled": {
        "address": 502,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "cooling_forced": {
        "address": 503,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # --- Service registers (Tab.50) ---
    "service_required": {
        "address": 512,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "service_notification": {
        "address": 513,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "hours_producing_since_service": {
        "address": 514,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 2,  # resolution: 2 hours
    },
    "hours_since_service": {
        "address": 515,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 2,  # resolution: 2 hours
    },
    "starts_since_service": {
        "address": 516,
        "type": REG_HOLDING,
        "count": 2,
        "data_type": "uint32",
        "scale": 1,
    },
    # --- Error registers (Tab.51-53) ---
    "error_present": {
        "address": 531,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "devices_connected": {
        "address": 128,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    # Per-board error codes (boards 1-4, most common setup)
    "board1_error_code": {
        "address": 532,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "board1_error_severity": {
        "address": 533,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "board2_error_code": {
        "address": 534,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "board2_error_severity": {
        "address": 535,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "board3_error_code": {
        "address": 536,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "board3_error_severity": {
        "address": 537,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "board4_error_code": {
        "address": 538,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
    "board4_error_severity": {
        "address": 539,
        "type": REG_HOLDING,
        "count": 1,
        "data_type": "uint16",
        "scale": 1,
    },
}

# ===== Static Sensor Definitions =====

_IWR_STATIC_SENSORS: Final = {
    # --- Device Information GTW-08 (from German spec 7740782-01) ---
    "gateway_device_type": {
        "register": "gateway_device_type",
        "translation_key": "gateway_device_type",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:chip",
    },
    # --- Zone Detection (Tab.24) ---
    "zone_count": {
        "register": "zone_count",
        "translation_key": "zone_count",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:counter",
    },
    # --- Zone Count Subtypes (from German spec 7740782-01) ---
    "zones_disabled": {
        "register": "zones_disabled",
        "translation_key": "zones_disabled",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:counter",
    },
    "zones_ch": {
        "register": "zones_ch",
        "translation_key": "zones_ch",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:counter",
    },
    "zones_ch_cooling": {
        "register": "zones_ch_cooling",
        "translation_key": "zones_ch_cooling",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:counter",
    },
    "zones_dhw": {
        "register": "zones_dhw",
        "translation_key": "zones_dhw",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:counter",
    },
    "zones_process_heat": {
        "register": "zones_process_heat",
        "translation_key": "zones_process_heat",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:counter",
    },
    "zones_swimming_pool": {
        "register": "zones_swimming_pool",
        "translation_key": "zones_swimming_pool",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:counter",
    },
    "zones_others": {
        "register": "zones_others",
        "translation_key": "zones_others",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:counter",
    },
    # --- Temperature and Power Control Sensors (Tab.18) ---
    "control_power": {
        "register": "control_power",
        "translation_key": "control_power",
        "device_class": None,
        "unit": "%",
        "state_class": "measurement",
        "icon": "mdi:gauge",
    },
    "control_temperature": {
        "register": "control_temperature",
        "translation_key": "control_temperature",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "control_algorithm_type": {
        "register": "control_algorithm_type",
        "translation_key": "control_algorithm_type",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:cog-outline",
        "enum_map": "iwr_algorithm_type",
    },
    "control_heat_demand_type": {
        "register": "control_heat_demand_type",
        "translation_key": "control_heat_demand_type",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:fire-circle",
        "enum_map": "iwr_heat_demand_type",
    },
    # --- Main Appliance Sensors ---
    "system_power": {
        "register": "system_power",
        "translation_key": "system_power",
        "device_class": None,
        "unit": "%",
        "state_class": "measurement",
        "icon": "mdi:gauge",
    },
    # --- Received Temperatures from CU (from German spec 7740782-01) ---
    "cu_flow_temperature": {
        "register": "cu_flow_temperature",
        "translation_key": "cu_flow_temperature",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "cu_return_temperature": {
        "register": "cu_return_temperature",
        "translation_key": "cu_return_temperature",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "outside_temperature": {
        "register": "outside_temperature",
        "translation_key": "outside_temperature",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "seasonal_mode": {
        "register": "seasonal_mode",
        "translation_key": "seasonal_mode",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:weather-partly-cloudy",
        "enum_map": "iwr_seasonal_mode",
    },
    # --- Appliance Parameters (from German spec 7740782-01) ---
    "summer_winter_threshold": {
        "register": "summer_winter_threshold",
        "translation_key": "summer_winter_threshold",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
        "icon": "mdi:thermometer-lines",
    },
    "neutral_band": {
        "register": "neutral_band",
        "translation_key": "neutral_band",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
        "icon": "mdi:thermometer-lines",
    },
    "frost_protection_threshold": {
        "register": "frost_protection_threshold",
        "translation_key": "frost_protection_threshold",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
        "icon": "mdi:snowflake-thermometer",
    },
    "force_summer_mode": {
        "register": "force_summer_mode",
        "translation_key": "force_summer_mode",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:weather-sunny",
        "enum_map": "iwr_on_off",
    },
    "flow_temperature": {
        "register": "flow_temperature",
        "translation_key": "flow_temperature",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "return_temperature": {
        "register": "return_temperature",
        "translation_key": "return_temperature",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "exhaust_gas_temperature": {
        "register": "exhaust_gas_temperature",
        "translation_key": "exhaust_gas_temperature",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "hp_flow_temperature": {
        "register": "hp_flow_temperature",
        "translation_key": "hp_flow_temperature",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "hp_return_temperature": {
        "register": "hp_return_temperature",
        "translation_key": "hp_return_temperature",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    # --- Internal Setpoints (from German spec 7740782-01) ---
    "internal_dhw_setpoint": {
        "register": "internal_dhw_setpoint",
        "translation_key": "internal_dhw_setpoint",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
        "icon": "mdi:water-thermometer",
    },
    "ch_setpoint": {
        "register": "ch_setpoint",
        "translation_key": "ch_setpoint",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
        "icon": "mdi:thermostat",
    },
    "cooling_setpoint": {
        "register": "cooling_setpoint",
        "translation_key": "cooling_setpoint",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
        "icon": "mdi:snowflake-thermometer",
    },
    "dhw_flow_setpoint": {
        "register": "dhw_flow_setpoint",
        "translation_key": "dhw_flow_setpoint",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "water_pressure": {
        "register": "water_pressure",
        "translation_key": "water_pressure",
        "device_class": "pressure",
        "unit": "bar",
        "state_class": "measurement",
    },
    "flow_rate": {
        "register": "flow_rate",
        "translation_key": "flow_rate",
        "device_class": None,
        "unit": "l/min",
        "state_class": "measurement",
        "icon": "mdi:water-pump",
    },
    "main_status": {
        "register": "main_status",
        "translation_key": "main_status",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:information-outline",
        "enum_map": "iwr_main_status",
    },
    "sub_status": {
        "register": "sub_status",
        "translation_key": "sub_status",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:information-outline",
        "enum_map": "iwr_sub_status",
    },
    "relative_power": {
        "register": "relative_power",
        "translation_key": "relative_power",
        "device_class": None,
        "unit": "%",
        "state_class": "measurement",
        "icon": "mdi:gauge",
    },
    "power_setpoint": {
        "register": "power_setpoint",
        "translation_key": "power_setpoint",
        "device_class": None,
        "unit": "%",
        "state_class": "measurement",
        "icon": "mdi:gauge",
    },
    "ionization_current": {
        "register": "ionization_current",
        "translation_key": "ionization_current",
        "device_class": None,
        "unit": "µA",
        "state_class": "measurement",
        "icon": "mdi:flash",
    },
    "pump_speed": {
        "register": "pump_speed",
        "translation_key": "pump_speed",
        "device_class": None,
        "unit": "%",
        "state_class": "measurement",
        "icon": "mdi:pump",
    },
    "actual_power": {
        "register": "actual_power",
        "translation_key": "actual_power",
        "device_class": "power",
        "unit": "kW",
        "state_class": "measurement",
    },
    "cop": {
        "register": "cop",
        "translation_key": "cop",
        "device_class": None,
        "unit": None,
        "state_class": "measurement",
        "icon": "mdi:chart-line",
    },
    "cop_threshold": {
        "register": "cop_threshold",
        "translation_key": "cop_threshold",
        "device_class": None,
        "unit": None,
        "state_class": "measurement",
        "icon": "mdi:chart-line",
    },
    # --- Cascade Flow/Return Temperature (Tab.23) ---
    "cascade_flow_temperature": {
        "register": "cascade_flow_temperature",
        "translation_key": "cascade_flow_temperature",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    "cascade_return_temperature": {
        "register": "cascade_return_temperature",
        "translation_key": "cascade_return_temperature",
        "device_class": "temperature",
        "unit": "°C",
        "state_class": "measurement",
    },
    # --- Counters & Energy ---
    "total_starts": {
        "register": "total_starts",
        "translation_key": "total_starts",
        "device_class": None,
        "unit": None,
        "state_class": "total_increasing",
        "icon": "mdi:counter",
    },
    "total_operating_hours": {
        "register": "total_operating_hours",
        "translation_key": "total_operating_hours",
        "device_class": "duration",
        "unit": "h",
        "state_class": "total_increasing",
        "icon": "mdi:clock-outline",
    },
    "backup1_starts": {
        "register": "backup1_starts",
        "translation_key": "backup1_starts",
        "device_class": None,
        "unit": None,
        "state_class": "total_increasing",
        "icon": "mdi:counter",
    },
    "backup1_operating_hours": {
        "register": "backup1_operating_hours",
        "translation_key": "backup1_operating_hours",
        "device_class": "duration",
        "unit": "h",
        "state_class": "total_increasing",
        "icon": "mdi:clock-outline",
    },
    "backup2_starts": {
        "register": "backup2_starts",
        "translation_key": "backup2_starts",
        "device_class": None,
        "unit": None,
        "state_class": "total_increasing",
        "icon": "mdi:counter",
    },
    "backup2_operating_hours": {
        "register": "backup2_operating_hours",
        "translation_key": "backup2_operating_hours",
        "device_class": "duration",
        "unit": "h",
        "state_class": "total_increasing",
        "icon": "mdi:clock-outline",
    },
    "mains_power_hours": {
        "register": "mains_power_hours",
        "translation_key": "mains_power_hours",
        "device_class": "duration",
        "unit": "h",
        "state_class": "total_increasing",
        "icon": "mdi:clock-outline",
    },
    "energy_consumed_ch": {
        "register": "energy_consumed_ch",
        "translation_key": "energy_consumed_ch",
        "device_class": "energy",
        "unit": "kWh",
        "state_class": "total_increasing",
    },
    "energy_consumed_dhw": {
        "register": "energy_consumed_dhw",
        "translation_key": "energy_consumed_dhw",
        "device_class": "energy",
        "unit": "kWh",
        "state_class": "total_increasing",
    },
    "energy_consumed_cooling": {
        "register": "energy_consumed_cooling",
        "translation_key": "energy_consumed_cooling",
        "device_class": "energy",
        "unit": "kWh",
        "state_class": "total_increasing",
    },
    "total_energy_consumed": {
        "register": "total_energy_consumed",
        "translation_key": "total_energy_consumed",
        "device_class": "energy",
        "unit": "kWh",
        "state_class": "total_increasing",
    },
    "energy_consumed_backup": {
        "register": "energy_consumed_backup",
        "translation_key": "energy_consumed_backup",
        "device_class": "energy",
        "unit": "kWh",
        "state_class": "total_increasing",
    },
    "total_thermal_delivered": {
        "register": "total_thermal_delivered",
        "translation_key": "total_thermal_delivered",
        "device_class": "energy",
        "unit": "kWh",
        "state_class": "total_increasing",
    },
    "thermal_delivered_ch": {
        "register": "thermal_delivered_ch",
        "translation_key": "thermal_delivered_ch",
        "device_class": "energy",
        "unit": "kWh",
        "state_class": "total_increasing",
    },
    "thermal_delivered_dhw": {
        "register": "thermal_delivered_dhw",
        "translation_key": "thermal_delivered_dhw",
        "device_class": "energy",
        "unit": "kWh",
        "state_class": "total_increasing",
    },
    "thermal_delivered_cooling": {
        "register": "thermal_delivered_cooling",
        "translation_key": "thermal_delivered_cooling",
        "device_class": "energy",
        "unit": "kWh",
        "state_class": "total_increasing",
    },
    "energy_delivered_backup": {
        "register": "energy_delivered_backup",
        "translation_key": "energy_delivered_backup",
        "device_class": "energy",
        "unit": "kWh",
        "state_class": "total_increasing",
    },
    # --- Appliance Enable/Disable (from German spec 7740782-01) ---
    "ch_enabled": {
        "register": "ch_enabled",
        "translation_key": "ch_enabled",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:radiator",
        "enum_map": "iwr_on_off",
    },
    "dhw_enabled": {
        "register": "dhw_enabled",
        "translation_key": "dhw_enabled",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:water-boiler",
        "enum_map": "iwr_on_off",
    },
    "cooling_enabled": {
        "register": "cooling_enabled",
        "translation_key": "cooling_enabled",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:snowflake",
        "enum_map": "iwr_cooling_enabled",
    },
    "cooling_forced": {
        "register": "cooling_forced",
        "translation_key": "cooling_forced",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:snowflake-alert",
        "enum_map": "iwr_on_off",
    },
    # --- Service sensors ---
    "service_notification": {
        "register": "service_notification",
        "translation_key": "service_notification",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:wrench",
        "enum_map": "iwr_service_notification",
    },
    "hours_producing_since_service": {
        "register": "hours_producing_since_service",
        "translation_key": "hours_producing_since_service",
        "device_class": "duration",
        "unit": "h",
        "state_class": "total_increasing",
        "icon": "mdi:clock-alert-outline",
    },
    "hours_since_service": {
        "register": "hours_since_service",
        "translation_key": "hours_since_service",
        "device_class": "duration",
        "unit": "h",
        "state_class": "total_increasing",
        "icon": "mdi:clock-alert-outline",
    },
    "starts_since_service": {
        "register": "starts_since_service",
        "translation_key": "starts_since_service",
        "device_class": None,
        "unit": None,
        "state_class": "total_increasing",
        "icon": "mdi:counter",
    },
    # --- Error sensors ---
    "devices_connected": {
        "register": "devices_connected",
        "translation_key": "devices_connected",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:developer-board",
    },
    "board1_error_code": {
        "register": "board1_error_code",
        "translation_key": "board1_error_code",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:alert-circle-outline",
    },
    "board1_error_severity": {
        "register": "board1_error_severity",
        "translation_key": "board1_error_severity",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:alert-circle-outline",
        "enum_map": "iwr_error_severity",
    },
    "board2_error_code": {
        "register": "board2_error_code",
        "translation_key": "board2_error_code",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:alert-circle-outline",
    },
    "board2_error_severity": {
        "register": "board2_error_severity",
        "translation_key": "board2_error_severity",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:alert-circle-outline",
        "enum_map": "iwr_error_severity",
    },
    "board3_error_code": {
        "register": "board3_error_code",
        "translation_key": "board3_error_code",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:alert-circle-outline",
    },
    "board3_error_severity": {
        "register": "board3_error_severity",
        "translation_key": "board3_error_severity",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:alert-circle-outline",
        "enum_map": "iwr_error_severity",
    },
    "board4_error_code": {
        "register": "board4_error_code",
        "translation_key": "board4_error_code",
        "device_class": None,
        "unit": None,
        "state_class": None,
        "icon": "mdi:alert-circle-outline",
    },
    "board4_error_severity": {
        "register": "board4_error_severity",
        "translation_key": "board4_error_severity",
        "device_class": "enum",
        "unit": None,
        "state_class": None,
        "icon": "mdi:alert-circle-outline",
        "enum_map": "iwr_error_severity",
    },
}

# ===== Static Binary Sensor Definitions =====

_IWR_STATIC_BINARY_SENSORS: Final = {
    # --- Bitfield 275: Heat demand ---
    "demand_direct_zones": {
        "register": "demand_direct_zones",
        "translation_key": "demand_direct_zones",
        "device_class": None,
        "icon": "mdi:radiator",
    },
    "demand_mixing_circuits": {
        "register": "demand_mixing_circuits",
        "translation_key": "demand_mixing_circuits",
        "device_class": None,
        "icon": "mdi:valve",
    },
    "demand_valves_open_safety": {
        "register": "demand_valves_open_safety",
        "translation_key": "demand_valves_open_safety",
        "device_class": None,
        "icon": "mdi:valve-open",
    },
    "demand_manual_heat": {
        "register": "demand_manual_heat",
        "translation_key": "demand_manual_heat",
        "device_class": None,
        "icon": "mdi:hand-back-right",
    },
    "demand_cooling_allowed": {
        "register": "demand_cooling_allowed",
        "translation_key": "demand_cooling_allowed",
        "device_class": None,
        "icon": "mdi:snowflake",
    },
    "demand_dhw_allowed": {
        "register": "demand_dhw_allowed",
        "translation_key": "demand_dhw_allowed",
        "device_class": None,
        "icon": "mdi:water-boiler",
    },
    "demand_heat_engine_active": {
        "register": "demand_heat_engine_active",
        "translation_key": "demand_heat_engine_active",
        "device_class": "running",
    },
    # --- Bitfield 279: Output status 1 ---
    "status_flame_on": {
        "register": "status_flame_on",
        "translation_key": "status_flame_on",
        "device_class": None,
        "icon": "mdi:fire",
    },
    "status_heat_pump_on": {
        "register": "status_heat_pump_on",
        "translation_key": "status_heat_pump_on",
        "device_class": "running",
    },
    "status_backup1_on": {
        "register": "status_backup1_on",
        "translation_key": "status_backup1_on",
        "device_class": "running",
    },
    "status_backup2_on": {
        "register": "status_backup2_on",
        "translation_key": "status_backup2_on",
        "device_class": "running",
    },
    "status_dhw_backup_on": {
        "register": "status_dhw_backup_on",
        "translation_key": "status_dhw_backup_on",
        "device_class": "running",
    },
    "status_service_required": {
        "register": "status_service_required",
        "translation_key": "status_service_required",
        "device_class": "problem",
    },
    "status_power_down_needed": {
        "register": "status_power_down_needed",
        "translation_key": "status_power_down_needed",
        "device_class": "problem",
    },
    "status_water_pressure_low": {
        "register": "status_water_pressure_low",
        "translation_key": "status_water_pressure_low",
        "device_class": "problem",
    },
    # --- Bitfield 280: Output status 2 ---
    "output_pump": {
        "register": "output_pump",
        "translation_key": "output_pump",
        "device_class": "running",
    },
    "output_3way_valve_open": {
        "register": "output_3way_valve_open",
        "translation_key": "output_3way_valve_open",
        "device_class": None,
        "icon": "mdi:valve-open",
    },
    "output_3way_valve": {
        "register": "output_3way_valve",
        "translation_key": "output_3way_valve",
        "device_class": None,
        "icon": "mdi:valve",
    },
    "output_3way_valve_closed": {
        "register": "output_3way_valve_closed",
        "translation_key": "output_3way_valve_closed",
        "device_class": None,
        "icon": "mdi:valve-closed",
    },
    "output_dhw_active": {
        "register": "output_dhw_active",
        "translation_key": "output_dhw_active",
        "device_class": "running",
    },
    "output_ch_active": {
        "register": "output_ch_active",
        "translation_key": "output_ch_active",
        "device_class": "running",
    },
    "output_cooling_active": {
        "register": "output_cooling_active",
        "translation_key": "output_cooling_active",
        "device_class": "running",
    },
    # --- Service / Error binary sensors ---
    "service_required": {
        "register": "service_required",
        "translation_key": "service_required",
        "device_class": "problem",
    },
    "error_present": {
        "register": "error_present",
        "translation_key": "error_present",
        "device_class": "problem",
    },
}


# ===== Dynamic Zone Generation =====


def _zone_addr(base: int, zone_idx: int) -> int:
    """Compute zone register address. base is zone-1 address, zone_idx is 0-based."""
    return base + ZONE_ADDR_OFFSET * zone_idx


def _build_zone_registers(zones: list[int]) -> dict[str, Any]:
    """Generate register map entries for the given zone numbers (1-based)."""
    registers: dict[str, Any] = {}
    for zn in zones:
        z = zn - 1  # 0-based index for address lookup
        prefix = f"zone{zn}"

        # CM040 - Zone flow temperature (INT16, 0.01°C)
        registers[f"{prefix}_flow_temp"] = {
            "address": ZONE_ADDRESSES["CM040"][z],
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "int16",
            "scale": IWR_SCALE_TEMP,
        }
        # CM070 - Zone flow temperature setpoint (UINT16, 0.01°C)
        registers[f"{prefix}_flow_setpoint"] = {
            "address": ZONE_ADDRESSES["CM070"][z],
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_TEMP,
        }
        # CM190 - Room temperature setpoint (INT16, 0.1°C)
        registers[f"{prefix}_room_setpoint"] = {
            "address": ZONE_ADDRESSES["CM190"][z],
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "int16",
            "scale": IWR_SCALE_ROOM_TEMP,
        }
        # CM130 - Current zone activity (ENUM8)
        registers[f"{prefix}_activity"] = {
            "address": ZONE_ADDRESSES["CM130"][z],
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": 1,
        }
        # CM120 - Zone operating mode (ENUM8)
        registers[f"{prefix}_operating_mode"] = {
            "address": ZONE_ADDRESSES["CM120"][z],
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": 1,
        }
        # CM050 - Zone pump status (UINT8, 0/1)
        registers[f"{prefix}_pump"] = {
            "address": ZONE_ADDRESSES["CM050"][z],
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "bool",
        }
        # CM010 - Zone flow measurement active (UINT8, 0/1)
        registers[f"{prefix}_flow_measurement"] = {
            "address": ZONE_ADDRESSES["CM010"][z],
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "bool",
        }
        # CC001 - Pump operating hours (UINT32)
        registers[f"{prefix}_pump_hours"] = {
            "address": ZONE_ADDRESSES["CC001"][z],
            "type": REG_HOLDING,
            "count": 2,
            "data_type": "uint32",
            "scale": 1,
        }
        # CC010 - Pump starts (UINT32)
        registers[f"{prefix}_pump_starts"] = {
            "address": ZONE_ADDRESSES["CC010"][z],
            "type": REG_HOLDING,
            "count": 2,
            "data_type": "uint32",
            "scale": 1,
        }
        # CP02X - Zone function type (ENUM8, Tab.25/26)
        registers[f"{prefix}_function"] = {
            "address": ZONE_ADDRESSES["CP02X"][z],
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": 1,
        }
        # DEV - Zone device type (UINT16 as 0xZZYY, Tab.25/26)
        registers[f"{prefix}_device_type"] = {
            "address": ZONE_ADDRESSES["DEV"][z],
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": 1,
        }
        # CP32X - Zone control mode (ENUM8, Tab.36/42)
        registers[f"{prefix}_control_mode"] = {
            "address": ZONE_ADDRESSES["CP32X"][z],
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": 1,
        }
        # CP01X - Zone fixed flow setpoint (UINT16, 0.01°C, Tab.37)
        registers[f"{prefix}_fixed_flow_setpoint"] = {
            "address": ZONE_ADDRESSES["CP01X"][z],
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_TEMP,
        }
        # CP20X - Zone room temp setpoint manual (UINT16, 0.1°C, Tab.43)
        registers[f"{prefix}_room_setpoint_manual"] = {
            "address": ZONE_ADDRESSES["CP20X"][z],
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_ROOM_TEMP,
        }
        # CP23X - Heating curve gradient (UINT8, resolution 0.1, Tab.39)
        registers[f"{prefix}_heating_curve_gradient"] = {
            "address": ZONE_ADDRESSES["CP23X"][z],
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": 0.1,
        }
        # CP21X - Heating curve footpoint (UINT16, 0.1°C, Tab.40)
        registers[f"{prefix}_heating_curve_footpoint"] = {
            "address": ZONE_ADDRESSES["CP21X"][z],
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_ROOM_TEMP,
        }

        # ===== New zone registers from German spec 7740782-01 =====

        # 640 - Zone type (ENUM8)
        registers[f"{prefix}_zone_type"] = {
            "address": _zone_addr(640, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": 1,
        }
        # 650-654 - Room comfort setpoints 1-5 (UINT16, 0.1°C)
        for sp in range(1, 6):
            registers[f"{prefix}_comfort_setpoint_{sp}"] = {
                "address": _zone_addr(649 + sp, z),
                "type": REG_HOLDING,
                "count": 1,
                "data_type": "uint16",
                "scale": IWR_SCALE_ROOM_TEMP,
            }
        # 655 - Night setback setpoint (UINT16, 0.1°C)
        registers[f"{prefix}_night_setback"] = {
            "address": _zone_addr(655, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_ROOM_TEMP,
        }
        # 656-660 - Room cooling setpoints 1-5 (UINT16, 0.1°C)
        for sp in range(1, 6):
            registers[f"{prefix}_cooling_room_setpoint_{sp}"] = {
                "address": _zone_addr(655 + sp, z),
                "type": REG_HOLDING,
                "count": 1,
                "data_type": "uint16",
                "scale": IWR_SCALE_ROOM_TEMP,
            }
        # 661 - Cooling night setback (UINT16, 0.1°C)
        registers[f"{prefix}_cooling_night_setback"] = {
            "address": _zone_addr(661, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_ROOM_TEMP,
        }
        # 662 - Holiday room setpoint (UINT16, 0.1°C)
        registers[f"{prefix}_holiday_setpoint"] = {
            "address": _zone_addr(662, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_ROOM_TEMP,
        }
        # 663 - Temporary room setpoint (UINT16, 0.1°C)
        registers[f"{prefix}_temporary_setpoint"] = {
            "address": _zone_addr(663, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_ROOM_TEMP,
        }
        # 665 - DHW comfort setpoint (UINT16, 0.01°C)
        registers[f"{prefix}_dhw_comfort_setpoint"] = {
            "address": _zone_addr(665, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_TEMP,
        }
        # 666 - DHW reduced setpoint (UINT16, 0.01°C)
        registers[f"{prefix}_dhw_reduced_setpoint"] = {
            "address": _zone_addr(666, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_TEMP,
        }
        # 667 - DHW holiday setpoint (UINT16, 0.01°C)
        registers[f"{prefix}_dhw_holiday_setpoint"] = {
            "address": _zone_addr(667, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_TEMP,
        }
        # 668 - DHW anti-legionella setpoint (UINT16, 0.01°C)
        registers[f"{prefix}_dhw_antilegionella_setpoint"] = {
            "address": _zone_addr(668, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_TEMP,
        }
        # 669 - Swimming pool setpoint (UINT16, 0.01°C)
        registers[f"{prefix}_swimming_pool_setpoint"] = {
            "address": _zone_addr(669, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_TEMP,
        }
        # 670 - Process heat setpoint (UINT16, 0.01°C)
        registers[f"{prefix}_process_heat_setpoint"] = {
            "address": _zone_addr(670, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_TEMP,
        }
        # 671 - Heating control strategy (ENUM8)
        registers[f"{prefix}_heating_control_strategy"] = {
            "address": _zone_addr(671, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": 1,
        }
        # 672 - Max flow temperature setpoint (UINT16, 0.01°C)
        registers[f"{prefix}_max_flow_setpoint"] = {
            "address": _zone_addr(672, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_TEMP,
        }
        # 673 - Cooling mixing circuit flow setpoint (UINT16, 0.01°C)
        registers[f"{prefix}_cooling_mixing_setpoint"] = {
            "address": _zone_addr(673, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_TEMP,
        }
        # 676 - Heating curve footpoint night (UINT16, 0.1°C)
        registers[f"{prefix}_heating_curve_footpoint_night"] = {
            "address": _zone_addr(676, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_ROOM_TEMP,
        }
        # 677 - Max preheat time (UINT16, minutes)
        registers[f"{prefix}_max_preheat_time"] = {
            "address": _zone_addr(677, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": 1,
        }
        # 678 - Mixing valve shift (UINT16, 0.01°C)
        registers[f"{prefix}_mixing_valve_shift"] = {
            "address": _zone_addr(678, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_TEMP,
        }
        # 679 - Mixing valve bandwidth (UINT16, 0.01°C)
        registers[f"{prefix}_mixing_valve_bandwidth"] = {
            "address": _zone_addr(679, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_TEMP,
        }
        # 680 - DHW hysteresis (UINT16, 0.01°C)
        registers[f"{prefix}_dhw_hysteresis"] = {
            "address": _zone_addr(680, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_TEMP,
        }
        # 681 - DHW calorifier offset (UINT16, 0.01°C)
        registers[f"{prefix}_dhw_calorifier_offset"] = {
            "address": _zone_addr(681, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_TEMP,
        }
        # 682 - DHW calorifier setpoint raise (UINT16, 0.01°C)
        registers[f"{prefix}_dhw_calorifier_raise"] = {
            "address": _zone_addr(682, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_TEMP,
        }
        # 683 - Process heat hysteresis (UINT16, 0.01°C)
        registers[f"{prefix}_process_heat_hysteresis"] = {
            "address": _zone_addr(683, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_TEMP,
        }
        # 684 - Process heat offset (UINT16, 0.01°C)
        registers[f"{prefix}_process_heat_offset"] = {
            "address": _zone_addr(684, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_TEMP,
        }
        # 685 - Process heat calorifier setpoint raise (UINT16, 0.01°C)
        registers[f"{prefix}_process_heat_calorifier_raise"] = {
            "address": _zone_addr(685, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_TEMP,
        }
        # 686 - DHW calorifier hysteresis (UINT16, 0.01°C)
        registers[f"{prefix}_dhw_calorifier_hysteresis"] = {
            "address": _zone_addr(686, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": IWR_SCALE_TEMP,
        }
        # 687 - Pump post-run delay (UINT8, minutes)
        registers[f"{prefix}_pump_post_run"] = {
            "address": _zone_addr(687, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": 1,
        }
        # 688 - Time program selected (ENUM8)
        registers[f"{prefix}_time_program_selected"] = {
            "address": _zone_addr(688, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": 1,
        }

        # ===== Zone measurements (from German spec 7740782-01) =====

        # 1103 - Zone outdoor temperature (INT16, 0.01°C)
        registers[f"{prefix}_outside_temp"] = {
            "address": _zone_addr(1103, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "int16",
            "scale": IWR_SCALE_TEMP,
        }
        # 1104 - Zone room temperature (INT16, 0.01°C)
        registers[f"{prefix}_room_temp"] = {
            "address": _zone_addr(1104, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "int16",
            "scale": IWR_SCALE_TEMP,
        }
        # 1105 - Zone room temperature measured (INT16, 0.1°C)
        registers[f"{prefix}_room_temp_measured"] = {
            "address": _zone_addr(1105, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "int16",
            "scale": IWR_SCALE_ROOM_TEMP,
        }
        # 1106 - Zone heat demand on/off (ENUM8, 0=off/1=on)
        registers[f"{prefix}_heat_demand"] = {
            "address": _zone_addr(1106, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "bool",
        }
        # 1109 - Zone current heating mode (ENUM8)
        registers[f"{prefix}_heating_mode"] = {
            "address": _zone_addr(1109, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": 1,
        }
        # 1112 - Mixing valve opening (ENUM8, 0=no/1=yes)
        registers[f"{prefix}_mixing_valve_opening"] = {
            "address": _zone_addr(1112, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "bool",
        }
        # 1113 - Swimming pool secondary pump (ENUM8, 0=off/1=on)
        registers[f"{prefix}_swimming_pool_pump"] = {
            "address": _zone_addr(1113, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "bool",
        }
        # 1114 - Electrical backup output (ENUM8, 0=off/1=on)
        registers[f"{prefix}_electrical_backup_output"] = {
            "address": _zone_addr(1114, z),
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "bool",
        }

    return registers


def _build_zone_sensors(zones: list[int]) -> dict[str, Any]:
    """Generate sensor definitions for the given zone numbers (1-based)."""
    sensors: dict[str, Any] = {}
    for zn in zones:
        prefix = f"zone{zn}"

        sensors[f"{prefix}_flow_temp"] = {
            "register": f"{prefix}_flow_temp",
            "translation_key": "zone_flow_temp",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "zone_number": zn,
        }
        sensors[f"{prefix}_flow_setpoint"] = {
            "register": f"{prefix}_flow_setpoint",
            "translation_key": "zone_flow_setpoint",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "zone_number": zn,
        }
        sensors[f"{prefix}_room_setpoint"] = {
            "register": f"{prefix}_room_setpoint",
            "translation_key": "zone_room_setpoint",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "zone_number": zn,
        }
        sensors[f"{prefix}_activity"] = {
            "register": f"{prefix}_activity",
            "translation_key": "zone_activity",
            "device_class": "enum",
            "unit": None,
            "state_class": None,
            "icon": "mdi:thermostat",
            "enum_map": "iwr_zone_activity",
            "zone_number": zn,
        }
        sensors[f"{prefix}_operating_mode"] = {
            "register": f"{prefix}_operating_mode",
            "translation_key": "zone_operating_mode",
            "device_class": "enum",
            "unit": None,
            "state_class": None,
            "icon": "mdi:cog",
            "enum_map": "iwr_zone_operating_mode",
            "zone_number": zn,
        }
        sensors[f"{prefix}_pump_hours"] = {
            "register": f"{prefix}_pump_hours",
            "translation_key": "zone_pump_hours",
            "device_class": "duration",
            "unit": "h",
            "state_class": "total_increasing",
            "icon": "mdi:clock-outline",
            "zone_number": zn,
        }
        sensors[f"{prefix}_pump_starts"] = {
            "register": f"{prefix}_pump_starts",
            "translation_key": "zone_pump_starts",
            "device_class": None,
            "unit": None,
            "state_class": "total_increasing",
            "icon": "mdi:counter",
            "zone_number": zn,
        }
        sensors[f"{prefix}_function"] = {
            "register": f"{prefix}_function",
            "translation_key": "zone_function",
            "device_class": "enum",
            "unit": None,
            "state_class": None,
            "icon": "mdi:information-outline",
            "enum_map": "iwr_zone_function",
            "zone_number": zn,
        }
        sensors[f"{prefix}_device_type"] = {
            "register": f"{prefix}_device_type",
            "translation_key": "zone_device_type",
            "device_class": None,
            "unit": None,
            "state_class": None,
            "icon": "mdi:developer-board",
            "zone_number": zn,
            "value_format": "device_type",
            "device_categories": IWR_DEVICE_CATEGORY,
        }
        sensors[f"{prefix}_control_mode"] = {
            "register": f"{prefix}_control_mode",
            "translation_key": "zone_control_mode",
            "device_class": "enum",
            "unit": None,
            "state_class": None,
            "icon": "mdi:cog",
            "enum_map": "iwr_zone_control_mode",
            "zone_number": zn,
        }
        sensors[f"{prefix}_fixed_flow_setpoint"] = {
            "register": f"{prefix}_fixed_flow_setpoint",
            "translation_key": "zone_fixed_flow_setpoint",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "zone_number": zn,
        }
        sensors[f"{prefix}_room_setpoint_manual"] = {
            "register": f"{prefix}_room_setpoint_manual",
            "translation_key": "zone_room_setpoint_manual",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "zone_number": zn,
        }
        sensors[f"{prefix}_heating_curve_gradient"] = {
            "register": f"{prefix}_heating_curve_gradient",
            "translation_key": "zone_heating_curve_gradient",
            "device_class": None,
            "unit": None,
            "state_class": "measurement",
            "icon": "mdi:chart-line",
            "zone_number": zn,
        }
        sensors[f"{prefix}_heating_curve_footpoint"] = {
            "register": f"{prefix}_heating_curve_footpoint",
            "translation_key": "zone_heating_curve_footpoint",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:chart-line",
            "zone_number": zn,
        }

        # ===== New zone sensors from German spec 7740782-01 =====

        sensors[f"{prefix}_zone_type"] = {
            "register": f"{prefix}_zone_type",
            "translation_key": "zone_type",
            "device_class": "enum",
            "unit": None,
            "state_class": None,
            "icon": "mdi:information-outline",
            "enum_map": "iwr_zone_type",
            "zone_number": zn,
        }
        for sp in range(1, 6):
            sensors[f"{prefix}_comfort_setpoint_{sp}"] = {
                "register": f"{prefix}_comfort_setpoint_{sp}",
                "translation_key": f"zone_comfort_setpoint_{sp}",
                "device_class": "temperature",
                "unit": "°C",
                "state_class": "measurement",
                "icon": "mdi:home-thermometer",
                "zone_number": zn,
            }
        sensors[f"{prefix}_night_setback"] = {
            "register": f"{prefix}_night_setback",
            "translation_key": "zone_night_setback",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:weather-night",
            "zone_number": zn,
        }
        for sp in range(1, 6):
            sensors[f"{prefix}_cooling_room_setpoint_{sp}"] = {
                "register": f"{prefix}_cooling_room_setpoint_{sp}",
                "translation_key": f"zone_cooling_room_setpoint_{sp}",
                "device_class": "temperature",
                "unit": "°C",
                "state_class": "measurement",
                "icon": "mdi:snowflake-thermometer",
                "zone_number": zn,
            }
        sensors[f"{prefix}_cooling_night_setback"] = {
            "register": f"{prefix}_cooling_night_setback",
            "translation_key": "zone_cooling_night_setback",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:snowflake-thermometer",
            "zone_number": zn,
        }
        sensors[f"{prefix}_holiday_setpoint"] = {
            "register": f"{prefix}_holiday_setpoint",
            "translation_key": "zone_holiday_setpoint",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:beach",
            "zone_number": zn,
        }
        sensors[f"{prefix}_temporary_setpoint"] = {
            "register": f"{prefix}_temporary_setpoint",
            "translation_key": "zone_temporary_setpoint",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:clock-fast",
            "zone_number": zn,
        }
        sensors[f"{prefix}_dhw_comfort_setpoint"] = {
            "register": f"{prefix}_dhw_comfort_setpoint",
            "translation_key": "zone_dhw_comfort_setpoint",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:water-thermometer",
            "zone_number": zn,
        }
        sensors[f"{prefix}_dhw_reduced_setpoint"] = {
            "register": f"{prefix}_dhw_reduced_setpoint",
            "translation_key": "zone_dhw_reduced_setpoint",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:water-thermometer",
            "zone_number": zn,
        }
        sensors[f"{prefix}_dhw_holiday_setpoint"] = {
            "register": f"{prefix}_dhw_holiday_setpoint",
            "translation_key": "zone_dhw_holiday_setpoint",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:water-thermometer",
            "zone_number": zn,
        }
        sensors[f"{prefix}_dhw_antilegionella_setpoint"] = {
            "register": f"{prefix}_dhw_antilegionella_setpoint",
            "translation_key": "zone_dhw_antilegionella_setpoint",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:bacteria-outline",
            "zone_number": zn,
        }
        sensors[f"{prefix}_swimming_pool_setpoint"] = {
            "register": f"{prefix}_swimming_pool_setpoint",
            "translation_key": "zone_swimming_pool_setpoint",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:pool-thermometer",
            "zone_number": zn,
        }
        sensors[f"{prefix}_process_heat_setpoint"] = {
            "register": f"{prefix}_process_heat_setpoint",
            "translation_key": "zone_process_heat_setpoint",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:fire",
            "zone_number": zn,
        }
        sensors[f"{prefix}_heating_control_strategy"] = {
            "register": f"{prefix}_heating_control_strategy",
            "translation_key": "zone_heating_control_strategy",
            "device_class": "enum",
            "unit": None,
            "state_class": None,
            "icon": "mdi:strategy",
            "enum_map": "iwr_heating_control_strategy",
            "zone_number": zn,
        }
        sensors[f"{prefix}_max_flow_setpoint"] = {
            "register": f"{prefix}_max_flow_setpoint",
            "translation_key": "zone_max_flow_setpoint",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:thermometer-chevron-up",
            "zone_number": zn,
        }
        sensors[f"{prefix}_cooling_mixing_setpoint"] = {
            "register": f"{prefix}_cooling_mixing_setpoint",
            "translation_key": "zone_cooling_mixing_setpoint",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:snowflake-thermometer",
            "zone_number": zn,
        }
        sensors[f"{prefix}_heating_curve_footpoint_night"] = {
            "register": f"{prefix}_heating_curve_footpoint_night",
            "translation_key": "zone_heating_curve_footpoint_night",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:chart-line",
            "zone_number": zn,
        }
        sensors[f"{prefix}_max_preheat_time"] = {
            "register": f"{prefix}_max_preheat_time",
            "translation_key": "zone_max_preheat_time",
            "device_class": None,
            "unit": "min",
            "state_class": "measurement",
            "icon": "mdi:clock-start",
            "zone_number": zn,
        }
        sensors[f"{prefix}_mixing_valve_shift"] = {
            "register": f"{prefix}_mixing_valve_shift",
            "translation_key": "zone_mixing_valve_shift",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:valve",
            "zone_number": zn,
        }
        sensors[f"{prefix}_mixing_valve_bandwidth"] = {
            "register": f"{prefix}_mixing_valve_bandwidth",
            "translation_key": "zone_mixing_valve_bandwidth",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:valve",
            "zone_number": zn,
        }
        sensors[f"{prefix}_dhw_hysteresis"] = {
            "register": f"{prefix}_dhw_hysteresis",
            "translation_key": "zone_dhw_hysteresis",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:water-thermometer",
            "zone_number": zn,
        }
        sensors[f"{prefix}_dhw_calorifier_offset"] = {
            "register": f"{prefix}_dhw_calorifier_offset",
            "translation_key": "zone_dhw_calorifier_offset",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:water-thermometer",
            "zone_number": zn,
        }
        sensors[f"{prefix}_dhw_calorifier_raise"] = {
            "register": f"{prefix}_dhw_calorifier_raise",
            "translation_key": "zone_dhw_calorifier_raise",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:water-thermometer",
            "zone_number": zn,
        }
        sensors[f"{prefix}_process_heat_hysteresis"] = {
            "register": f"{prefix}_process_heat_hysteresis",
            "translation_key": "zone_process_heat_hysteresis",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:fire",
            "zone_number": zn,
        }
        sensors[f"{prefix}_process_heat_offset"] = {
            "register": f"{prefix}_process_heat_offset",
            "translation_key": "zone_process_heat_offset",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:fire",
            "zone_number": zn,
        }
        sensors[f"{prefix}_process_heat_calorifier_raise"] = {
            "register": f"{prefix}_process_heat_calorifier_raise",
            "translation_key": "zone_process_heat_calorifier_raise",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:fire",
            "zone_number": zn,
        }
        sensors[f"{prefix}_dhw_calorifier_hysteresis"] = {
            "register": f"{prefix}_dhw_calorifier_hysteresis",
            "translation_key": "zone_dhw_calorifier_hysteresis",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:water-thermometer",
            "zone_number": zn,
        }
        sensors[f"{prefix}_pump_post_run"] = {
            "register": f"{prefix}_pump_post_run",
            "translation_key": "zone_pump_post_run",
            "device_class": None,
            "unit": "min",
            "state_class": "measurement",
            "icon": "mdi:pump",
            "zone_number": zn,
        }
        sensors[f"{prefix}_time_program_selected"] = {
            "register": f"{prefix}_time_program_selected",
            "translation_key": "zone_time_program_selected",
            "device_class": "enum",
            "unit": None,
            "state_class": None,
            "icon": "mdi:clock-outline",
            "enum_map": "iwr_time_program_selected",
            "zone_number": zn,
        }

        # ===== Zone measurements (from German spec 7740782-01) =====

        sensors[f"{prefix}_outside_temp"] = {
            "register": f"{prefix}_outside_temp",
            "translation_key": "zone_outside_temp",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "zone_number": zn,
        }
        sensors[f"{prefix}_room_temp"] = {
            "register": f"{prefix}_room_temp",
            "translation_key": "zone_room_temp",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:home-thermometer",
            "zone_number": zn,
        }
        sensors[f"{prefix}_room_temp_measured"] = {
            "register": f"{prefix}_room_temp_measured",
            "translation_key": "zone_room_temp_measured",
            "device_class": "temperature",
            "unit": "°C",
            "state_class": "measurement",
            "icon": "mdi:home-thermometer",
            "zone_number": zn,
        }
        sensors[f"{prefix}_heating_mode"] = {
            "register": f"{prefix}_heating_mode",
            "translation_key": "zone_heating_mode",
            "device_class": "enum",
            "unit": None,
            "state_class": None,
            "icon": "mdi:thermostat",
            "enum_map": "iwr_zone_heating_mode",
            "zone_number": zn,
        }

    return sensors


def _build_zone_binary_sensors(zones: list[int]) -> dict[str, Any]:
    """Generate binary sensor definitions for the given zone numbers (1-based)."""
    binary_sensors: dict[str, Any] = {}
    for zn in zones:
        prefix = f"zone{zn}"

        binary_sensors[f"{prefix}_pump"] = {
            "register": f"{prefix}_pump",
            "translation_key": "zone_pump",
            "device_class": "running",
            "zone_number": zn,
        }
        binary_sensors[f"{prefix}_flow_measurement"] = {
            "register": f"{prefix}_flow_measurement",
            "translation_key": "zone_flow_measurement",
            "device_class": None,
            "icon": "mdi:thermometer-check",
            "zone_number": zn,
        }

        # ===== Zone binary measurements (from German spec 7740782-01) =====

        binary_sensors[f"{prefix}_heat_demand"] = {
            "register": f"{prefix}_heat_demand",
            "translation_key": "zone_heat_demand",
            "device_class": "heat",
            "zone_number": zn,
        }
        binary_sensors[f"{prefix}_mixing_valve_opening"] = {
            "register": f"{prefix}_mixing_valve_opening",
            "translation_key": "zone_mixing_valve_opening",
            "device_class": None,
            "icon": "mdi:valve-open",
            "zone_number": zn,
        }
        binary_sensors[f"{prefix}_swimming_pool_pump"] = {
            "register": f"{prefix}_swimming_pool_pump",
            "translation_key": "zone_swimming_pool_pump",
            "device_class": "running",
            "icon": "mdi:pool",
            "zone_number": zn,
        }
        binary_sensors[f"{prefix}_electrical_backup_output"] = {
            "register": f"{prefix}_electrical_backup_output",
            "translation_key": "zone_electrical_backup_output",
            "device_class": "running",
            "icon": "mdi:lightning-bolt",
            "zone_number": zn,
        }

    return binary_sensors


# ===== Board Info Builders (System Discovery, addresses 129-188) =====

_BOARD_COUNT: Final = 10  # GTW-08 supports up to 10 electronic boards


def _build_board_registers() -> dict[str, Any]:
    """Generate register definitions for board info (boards 1..10).

    Each board occupies 6 registers starting at 129 + 6*(n-1):
      DeviceType (uint16), SoftwareVersion (uint16),
      ConfigTableVersion (uint16), HardwareVersion (uint16),
      ArticleNumber (uint32 = 2 registers).
    """
    registers: dict[str, Any] = {}
    for n in range(1, _BOARD_COUNT + 1):
        base = 129 + 6 * (n - 1)
        prefix = f"board{n}"

        registers[f"{prefix}_device_type"] = {
            "address": base,
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": 1,
        }
        registers[f"{prefix}_software_version"] = {
            "address": base + 1,
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": 1,
        }
        registers[f"{prefix}_config_table_version"] = {
            "address": base + 2,
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": 1,
        }
        registers[f"{prefix}_hardware_version"] = {
            "address": base + 3,
            "type": REG_HOLDING,
            "count": 1,
            "data_type": "uint16",
            "scale": 1,
        }
        registers[f"{prefix}_article_number"] = {
            "address": base + 4,
            "type": REG_HOLDING,
            "count": 2,
            "data_type": "uint32",
            "scale": 1,
        }

    return registers


def _build_board_sensors() -> dict[str, Any]:
    """Generate sensor definitions for board info (boards 1..10)."""
    sensors: dict[str, Any] = {}
    for n in range(1, _BOARD_COUNT + 1):
        prefix = f"board{n}"

        sensors[f"{prefix}_device_type"] = {
            "register": f"{prefix}_device_type",
            "translation_key": "board_device_type",
            "device_class": None,
            "unit": None,
            "state_class": None,
            "icon": "mdi:chip",
            "board_number": n,
        }
        sensors[f"{prefix}_software_version"] = {
            "register": f"{prefix}_software_version",
            "translation_key": "board_software_version",
            "device_class": None,
            "unit": None,
            "state_class": None,
            "icon": "mdi:memory",
            "board_number": n,
        }
        sensors[f"{prefix}_config_table_version"] = {
            "register": f"{prefix}_config_table_version",
            "translation_key": "board_config_table_version",
            "device_class": None,
            "unit": None,
            "state_class": None,
            "icon": "mdi:memory",
            "board_number": n,
        }
        sensors[f"{prefix}_hardware_version"] = {
            "register": f"{prefix}_hardware_version",
            "translation_key": "board_hardware_version",
            "device_class": None,
            "unit": None,
            "state_class": None,
            "icon": "mdi:memory",
            "board_number": n,
        }
        sensors[f"{prefix}_article_number"] = {
            "register": f"{prefix}_article_number",
            "translation_key": "board_article_number",
            "device_class": None,
            "unit": None,
            "state_class": None,
            "icon": "mdi:barcode",
            "board_number": n,
        }

    return sensors


# ===== Public API =====


def _build_entity_classification(
    sensors: dict[str, Any],
    binary_sensors: dict[str, Any],
) -> dict[str, tuple[str | None, bool]]:
    """Build a merged classification map for all IWR entities.

    Static entities are looked up by entity key in IWR_STATIC_ENTITY_CLASSIFICATION.
    Zone entities are looked up by translation_key in IWR_ZONE_ENTITY_CLASSIFICATION.
    Board entities all get IWR_BOARD_ENTITY_CLASSIFICATION.
    """
    classification: dict[str, tuple[str | None, bool]] = {}

    for entity_key, config in {**sensors, **binary_sensors}.items():
        translation_key = config.get("translation_key", entity_key)

        if entity_key in IWR_STATIC_ENTITY_CLASSIFICATION:
            classification[entity_key] = IWR_STATIC_ENTITY_CLASSIFICATION[entity_key]
        elif translation_key in IWR_ZONE_ENTITY_CLASSIFICATION:
            classification[entity_key] = IWR_ZONE_ENTITY_CLASSIFICATION[translation_key]
        elif translation_key.startswith("board_"):
            classification[entity_key] = IWR_BOARD_ENTITY_CLASSIFICATION
        # else: defaults to (None, True) at lookup time

    return classification


def get_iwr_device_config(zones: list[int] | None = None) -> dict[str, Any]:
    """Build the complete IWR device config for the given zone numbers (1-based)."""
    if zones is None:
        zones = [1]
    # Merge static + dynamic registers
    register_map = {
        **_IWR_STATIC_REGISTER_MAP,
        **_build_zone_registers(zones),
        **_build_board_registers(),
    }
    sensors = {
        **_IWR_STATIC_SENSORS,
        **_build_zone_sensors(zones),
        **_build_board_sensors(),
    }
    binary_sensors = {
        **_IWR_STATIC_BINARY_SENSORS,
        **_build_zone_binary_sensors(zones),
    }

    return {
        "register_map": register_map,
        "sensors": sensors,
        "binary_sensors": binary_sensors,
        "enum_maps": IWR_ENUM_MAPS,
        "entity_classification": _build_entity_classification(sensors, binary_sensors),
    }
