# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
d = datetime(2008, 1, 31)
assert (d + DateOffset(months=1)) == datetime(2008, 2, 29)
