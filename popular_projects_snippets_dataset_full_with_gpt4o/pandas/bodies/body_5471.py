# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
# specifically non-Tick offset
off = offsets.YearEnd(1)
result = ts_tz + off

assert isinstance(result, Timestamp)
assert result._creso == ts_tz._creso
if ts_tz.month == 12 and ts_tz.day == 31:
    assert result.year == ts_tz.year + 1
else:
    assert result.year == ts_tz.year
assert result.day == 31
assert result.month == 12
assert tz_compare(result.tz, ts_tz.tz)

result = ts_tz - off

assert isinstance(result, Timestamp)
assert result._creso == ts_tz._creso
assert result.year == ts_tz.year - 1
assert result.day == 31
assert result.month == 12
assert tz_compare(result.tz, ts_tz.tz)
