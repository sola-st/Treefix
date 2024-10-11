# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_week.py
weekday, dt, expected = case
offset = LastWeekOfMonth(weekday=weekday)
assert offset.is_on_offset(dt) == expected
