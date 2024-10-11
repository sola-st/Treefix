# Extracted from ./data/repos/pandas/pandas/tests/scalar/timedelta/test_timedelta.py
td = Timedelta(microseconds=1500)
res = td.as_unit("ms")

expected = Timedelta(milliseconds=1)
assert res == expected

assert res._creso == NpyDatetimeUnit.NPY_FR_ms.value
assert res.value == 1

with pytest.raises(ValueError, match="Cannot losslessly convert units"):
    td.as_unit("ms", round_ok=False)
