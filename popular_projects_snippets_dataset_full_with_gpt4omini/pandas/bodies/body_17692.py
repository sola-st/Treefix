# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/common.py
actual = offset.is_on_offset(date)
assert actual == expected, (
    f"\nExpected: {expected}\nActual: {actual}\nFor Offset: {offset})"
    f"\nAt Date: {date}"
)
