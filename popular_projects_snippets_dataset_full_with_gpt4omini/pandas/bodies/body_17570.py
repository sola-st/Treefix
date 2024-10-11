# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_hour.py
expected = Timestamp("2014-07-01 13:00")

assert dt + BusinessHour() * 3 == expected
assert dt + BusinessHour(n=3) == expected
