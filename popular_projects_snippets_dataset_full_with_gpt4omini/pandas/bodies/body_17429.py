# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py
offset = CustomBusinessHour(start="10:00", end="15:00", holidays=holidays)
assert offset.is_on_offset(dt) == expected
