# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
ts = Timestamp("1970-01-01").as_unit("ns")
assert ts.unit == "ns"

assert ts.as_unit("ns") is ts

res = ts.as_unit("us")
assert res.value == ts.value // 1000
assert res._creso == NpyDatetimeUnit.NPY_FR_us.value

rt = res.as_unit("ns")
assert rt.value == ts.value
assert rt._creso == ts._creso

res = ts.as_unit("ms")
assert res.value == ts.value // 1_000_000
assert res._creso == NpyDatetimeUnit.NPY_FR_ms.value

rt = res.as_unit("ns")
assert rt.value == ts.value
assert rt._creso == ts._creso

res = ts.as_unit("s")
assert res.value == ts.value // 1_000_000_000
assert res._creso == NpyDatetimeUnit.NPY_FR_s.value

rt = res.as_unit("ns")
assert rt.value == ts.value
assert rt._creso == ts._creso
