# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_quarter.py
# corner
offset = BQuarterBegin(n=-1, startingMonth=1)
assert datetime(2007, 4, 3) + offset == datetime(2007, 4, 2)
