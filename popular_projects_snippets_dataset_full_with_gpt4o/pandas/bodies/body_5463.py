# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
tz = tz_aware_fixture
tz = maybe_get_tz(tz)
ts = Timestamp._from_value_and_reso(ts.value, ts._creso, tz)
rt = tm.round_trip_pickle(ts)
assert rt._creso == ts._creso
assert rt == ts
