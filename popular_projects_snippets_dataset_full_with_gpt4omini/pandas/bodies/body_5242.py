# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py

v = Timedelta("1 days 10:11:12.0123456")
v_p = tm.round_trip_pickle(v)
assert v == v_p
