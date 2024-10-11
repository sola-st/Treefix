# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
ts = ts_tz

res = ts + np.timedelta64(1, "ns")
exp = ts.as_unit("ns") + np.timedelta64(1, "ns")
assert exp == res
assert exp._creso == NpyDatetimeUnit.NPY_FR_ns.value
