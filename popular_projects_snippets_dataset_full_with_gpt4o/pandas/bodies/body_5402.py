# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
# Gh 7825
t = Timestamp("2013-11-3", tz="America/Chicago").as_unit(unit)
result = t.replace(hour=3)
expected = Timestamp("2013-11-3 03:00:00", tz="America/Chicago")
assert result == expected
assert result._creso == getattr(NpyDatetimeUnit, f"NPY_FR_{unit}").value
