# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
# GH 18946 round near "fall back" DST
ts = Timestamp("2017-10-29 00:00:00", tz="UTC").tz_convert("Europe/Madrid")
ts = ts.as_unit(unit)
#
result = getattr(ts, method)("H", ambiguous=True)
assert result == ts
assert result._creso == getattr(NpyDatetimeUnit, f"NPY_FR_{unit}").value

result = getattr(ts, method)("H", ambiguous=False)
expected = Timestamp("2017-10-29 01:00:00", tz="UTC").tz_convert(
    "Europe/Madrid"
)
assert result == expected
assert result._creso == getattr(NpyDatetimeUnit, f"NPY_FR_{unit}").value

result = getattr(ts, method)("H", ambiguous="NaT")
assert result is NaT

msg = "Cannot infer dst time"
with pytest.raises(pytz.AmbiguousTimeError, match=msg):
    getattr(ts, method)("H", ambiguous="raise")
