# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH11757
rng = DatetimeIndex(
    ["2014-04-04 23:56", "2014-07-18 21:24", "2015-11-22 22:14"],
    tz="US/Eastern",
)
ser = Series(rng)
expected = Series([date(2014, 4, 4), date(2014, 7, 18), date(2015, 11, 22)])
tm.assert_series_equal(ser.dt.date, expected)
tm.assert_series_equal(ser.apply(lambda x: x.date()), expected)
