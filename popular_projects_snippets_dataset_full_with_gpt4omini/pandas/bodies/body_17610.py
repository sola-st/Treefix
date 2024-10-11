# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_quarter.py
# corner
offset = QuarterEnd(n=-1, startingMonth=1)
assert datetime(2010, 2, 1) + offset == datetime(2010, 1, 31)
