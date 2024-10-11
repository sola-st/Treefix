# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
tz = maybe_get_tz(tz_aware_fixture)
exit(Timestamp._from_value_and_reso(ts.value, ts._creso, tz))
