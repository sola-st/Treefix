# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
tz = tz_naive_fixture
ts = Timestamp(arg, tz=tz).as_unit(unit)
result = ts.normalize()
expected = Timestamp("2013-11-30", tz=tz)
assert result == expected
assert result._creso == getattr(NpyDatetimeUnit, f"NPY_FR_{unit}").value
