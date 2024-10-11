# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_arithmetic.py
dt = datetime(2013, 10, 12)
ts = Timestamp(datetime(2013, 10, 13))
assert (ts - dt).days == 1
assert (dt - ts).days == -1
