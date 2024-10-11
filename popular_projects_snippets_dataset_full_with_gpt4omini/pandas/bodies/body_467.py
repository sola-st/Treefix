# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_dtypes.py
res = DatetimeTZDtype("ms", "US/Eastern")
assert res.unit == "ms"
assert res._creso == NpyDatetimeUnit.NPY_FR_ms.value
assert res.str == "|M8[ms]"
assert str(res) == "datetime64[ms, US/Eastern]"
