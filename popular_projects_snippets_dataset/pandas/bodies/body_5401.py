# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
# GH#18319 check that 1) timezone is correctly normalized and
# 2) that hour is not incorrectly changed by this normalization
ts_naive = Timestamp("2017-12-03 16:03:30")
ts_aware = conversion.localize_pydatetime(ts_naive, tz)

# Preliminary sanity-check
assert ts_aware == normalize(ts_aware)

# Replace across DST boundary
ts2 = ts_aware.replace(month=6)

# Check that `replace` preserves hour literal
assert (ts2.hour, ts2.minute) == (ts_aware.hour, ts_aware.minute)

# Check that post-replace object is appropriately normalized
ts2b = normalize(ts2)
assert ts2 == ts2b
