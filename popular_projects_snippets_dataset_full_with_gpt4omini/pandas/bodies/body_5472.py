# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
# case with non-lossy rounding
ts = ts_tz

# choose a unit for `other` that doesn't match ts_tz's;
#  this construction ensures we get cases with other._creso < ts._creso
#  and cases with other._creso > ts._creso
unit = {
    NpyDatetimeUnit.NPY_FR_us.value: "ms",
    NpyDatetimeUnit.NPY_FR_ms.value: "s",
    NpyDatetimeUnit.NPY_FR_s.value: "us",
}[ts._creso]
other = ts.as_unit(unit)
assert other._creso != ts._creso

result = ts - other
assert isinstance(result, Timedelta)
assert result.value == 0
assert result._creso == max(ts._creso, other._creso)

result = other - ts
assert isinstance(result, Timedelta)
assert result.value == 0
assert result._creso == max(ts._creso, other._creso)

if ts._creso < other._creso:
    # Case where rounding is lossy
    other2 = other + Timedelta._from_value_and_reso(1, other._creso)
    exp = ts.as_unit(other.unit) - other2

    res = ts - other2
    assert res == exp
    assert res._creso == max(ts._creso, other._creso)

    res = other2 - ts
    assert res == -exp
    assert res._creso == max(ts._creso, other._creso)
else:
    ts2 = ts + Timedelta._from_value_and_reso(1, ts._creso)
    exp = ts2 - other.as_unit(ts2.unit)

    res = ts2 - other
    assert res == exp
    assert res._creso == max(ts._creso, other._creso)
    res = other - ts2
    assert res == -exp
    assert res._creso == max(ts._creso, other._creso)
