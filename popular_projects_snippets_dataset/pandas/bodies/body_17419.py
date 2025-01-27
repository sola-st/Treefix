# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_hour.py
expected = Timestamp("2014-07-01 13:00")

assert dt + CustomBusinessHour() * 3 == expected
assert dt + CustomBusinessHour(n=3) == expected
