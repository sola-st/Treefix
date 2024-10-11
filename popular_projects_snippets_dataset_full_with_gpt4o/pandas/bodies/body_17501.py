# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_week.py
week, weekday, dt, expected = case
offset = WeekOfMonth(week=week, weekday=weekday)
assert offset.is_on_offset(dt) == expected
