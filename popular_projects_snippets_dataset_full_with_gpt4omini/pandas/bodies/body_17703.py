# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_business_day.py
assert offset2 + dt == datetime(2008, 1, 3)
assert offset2 + np.datetime64("2008-01-01 00:00:00") == datetime(2008, 1, 3)
