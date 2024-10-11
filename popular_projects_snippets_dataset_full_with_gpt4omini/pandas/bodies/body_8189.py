# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_timezones.py
# GH 8917
tz = tz_type + tz
if isinstance(shift, str):
    shift = "shift_" + shift
dti = DatetimeIndex([Timestamp(start_ts)])
result = dti.tz_localize(tz, nonexistent=shift)
expected = DatetimeIndex([Timestamp(end_ts)]).tz_localize(tz)
tm.assert_index_equal(result, expected)
