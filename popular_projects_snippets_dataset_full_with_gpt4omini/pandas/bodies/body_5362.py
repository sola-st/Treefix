# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timezones.py
# GH 8917, 24466
tz = tz_type + tz
if isinstance(shift, str):
    shift = "shift_" + shift
ts = Timestamp(start_ts).as_unit(unit)
result = ts.tz_localize(tz, nonexistent=shift)
expected = Timestamp(end_ts).tz_localize(tz)

if unit == "us":
    assert result == expected.replace(nanosecond=0)
elif unit == "ms":
    micros = expected.microsecond - expected.microsecond % 1000
    assert result == expected.replace(microsecond=micros, nanosecond=0)
elif unit == "s":
    assert result == expected.replace(microsecond=0, nanosecond=0)
else:
    assert result == expected
assert result._creso == getattr(NpyDatetimeUnit, f"NPY_FR_{unit}").value
