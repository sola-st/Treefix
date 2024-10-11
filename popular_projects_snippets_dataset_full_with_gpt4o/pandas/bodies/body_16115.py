# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH21358
tz = maybe_get_tz(tz_naive_fixture)

dtindex = DatetimeIndex(
    ["2014-04-04 23:56", "2014-07-18 21:24", "2015-11-22 22:14"], tz=tz
)
ser = Series(dtindex)
expected = Series(
    [time(23, 56, tzinfo=tz), time(21, 24, tzinfo=tz), time(22, 14, tzinfo=tz)]
)
result = ser.dt.timetz
tm.assert_series_equal(result, expected)
