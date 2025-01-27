# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_hour.py
assert offset1 + dt == datetime(2014, 7, 1, 11)
assert offset2 + dt == datetime(2014, 7, 1, 13)
assert offset3 + dt == datetime(2014, 6, 30, 17)
assert offset4 + dt == datetime(2014, 6, 30, 14)
assert offset8 + dt == datetime(2014, 7, 1, 11)
assert offset9 + dt == datetime(2014, 7, 1, 22)
assert offset10 + dt == datetime(2014, 7, 1, 1)
