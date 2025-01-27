# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_qcut.py
# see gh-19872
tz = "US/Eastern"
ser = Series(date_range("20130101", periods=3, tz=tz))

result = qcut(ser, bins)
expected = Series(
    IntervalIndex(
        [
            Interval(
                Timestamp("2012-12-31 23:59:59.999999999", tz=tz),
                Timestamp("2013-01-01 16:00:00", tz=tz),
            ),
            Interval(
                Timestamp("2013-01-01 16:00:00", tz=tz),
                Timestamp("2013-01-02 08:00:00", tz=tz),
            ),
            Interval(
                Timestamp("2013-01-02 08:00:00", tz=tz),
                Timestamp("2013-01-03 00:00:00", tz=tz),
            ),
        ]
    )
).astype(CDT(ordered=True))
tm.assert_series_equal(result, expected)
