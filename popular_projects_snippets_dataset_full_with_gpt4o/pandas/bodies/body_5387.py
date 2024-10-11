# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_unary_ops.py
# GH 23324 round near "spring forward" DST
ts = Timestamp(ts_str, tz="America/Chicago").as_unit(unit)
result = getattr(ts, method)(freq, nonexistent="shift_forward")
expected = Timestamp("2018-03-11 03:00:00", tz="America/Chicago")
assert result == expected
assert result._creso == getattr(NpyDatetimeUnit, f"NPY_FR_{unit}").value

result = getattr(ts, method)(freq, nonexistent="NaT")
assert result is NaT

msg = "2018-03-11 02:00:00"
with pytest.raises(pytz.NonExistentTimeError, match=msg):
    getattr(ts, method)(freq, nonexistent="raise")
