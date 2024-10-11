# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
td = Timedelta(days=1)

assert td.as_unit("ns") is td

res = td.as_unit("us")
assert res.value == td.value // 1000
assert res._creso == NpyDatetimeUnit.NPY_FR_us.value

rt = res.as_unit("ns")
assert rt.value == td.value
assert rt._creso == td._creso

res = td.as_unit("ms")
assert res.value == td.value // 1_000_000
assert res._creso == NpyDatetimeUnit.NPY_FR_ms.value

rt = res.as_unit("ns")
assert rt.value == td.value
assert rt._creso == td._creso

res = td.as_unit("s")
assert res.value == td.value // 1_000_000_000
assert res._creso == NpyDatetimeUnit.NPY_FR_s.value

rt = res.as_unit("ns")
assert rt.value == td.value
assert rt._creso == td._creso
