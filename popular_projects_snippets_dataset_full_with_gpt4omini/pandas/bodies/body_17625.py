# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_custom_business_month.py
unpickled = tm.round_trip_pickle(obj)
assert unpickled == obj
