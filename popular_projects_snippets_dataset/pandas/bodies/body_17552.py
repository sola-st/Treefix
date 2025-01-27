# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_quarter.py
# corner
offset = BQuarterEnd(n=-1, startingMonth=1)
assert datetime(2010, 1, 31) + offset == datetime(2010, 1, 29)
