"""Codec for the GTW-08 ``Time_Of_Day`` timestamp format.

The GTW-08 specification describes timestamp registers (for example
"End change mode Time", CP-parameter register 978 for zone 1) as::

    Absolute time in milliseconds after midnight and the number of days
    since January 1, 1984.   Timestamp format: Time_Of_Day

This is the CANopen ``TIME_OF_DAY`` layout: 6 bytes made of a 32-bit
millisecond counter (only 28 bits used) followed by a 16-bit day counter.
Modbus transports it as 3 consecutive 16-bit registers.

The specification does NOT state the byte order of the two multi-byte
fields, nor whether the time is local time or UTC. The defaults below
(big-endian, local time) are the most common choice for Modbus gateways but
are still to be verified against a real device, e.g. by reading the register
while the app boost is active:

    action: broetje_heating.debug_read_register
    data: {address: 1490, count: 3, data_type: time_of_day}

The debug read service decodes the words with *both* byte orders so the
plausible one is obvious. If the device turns out to use little-endian,
change ``TIME_OF_DAY_BYTE_ORDER``.
"""

from __future__ import annotations

from datetime import date, datetime, time, timedelta
from typing import Final, Literal

ByteOrder = Literal["big", "little"]

TIME_OF_DAY_BYTE_ORDER: Final[ByteOrder] = "big"
TIME_OF_DAY_WORDS: Final = 3

_EPOCH: Final = date(1984, 1, 1)
_MS_PER_DAY: Final = 86_400_000
_MAX_DAYS: Final = 0xFFFF


def decode_time_of_day(
    words: list[int], byte_order: ByteOrder = TIME_OF_DAY_BYTE_ORDER
) -> datetime | None:
    """Decode 3 register words into a naive datetime.

    Returns None for "not set" patterns (all zero or all 0xFFFF) and for
    values that are not a valid time of day, which also makes a wrong byte
    order easy to spot.
    """
    if len(words) != TIME_OF_DAY_WORDS:
        return None
    if all(w == 0 for w in words) or all(w == 0xFFFF for w in words):
        return None

    raw = b"".join(w.to_bytes(2, "big") for w in words)
    millis = int.from_bytes(raw[:4], byte_order)
    days = int.from_bytes(raw[4:], byte_order)

    if millis >= _MS_PER_DAY:
        return None
    try:
        day = _EPOCH + timedelta(days=days)
    except OverflowError:
        return None
    return datetime.combine(day, time()) + timedelta(milliseconds=millis)


def encode_time_of_day(
    value: datetime, byte_order: ByteOrder = TIME_OF_DAY_BYTE_ORDER
) -> list[int]:
    """Encode a naive datetime into 3 register words."""
    days = (value.date() - _EPOCH).days
    if not 0 <= days <= _MAX_DAYS:
        raise ValueError(f"{value} is outside the Time_Of_Day range")

    midnight = datetime.combine(value.date(), time())
    millis = int((value - midnight).total_seconds() * 1000)

    raw = millis.to_bytes(4, byte_order) + days.to_bytes(2, byte_order)
    return [int.from_bytes(raw[i : i + 2], "big") for i in range(0, 6, 2)]
