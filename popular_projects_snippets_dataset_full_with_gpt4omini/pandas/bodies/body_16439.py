# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_cut.py
# see gh-14714
#
# Testing time data when it comes in various collection types.
result, _ = cut(data, 3, retbins=True)
expected = Series(
    IntervalIndex(
        [
            Interval(
                Timestamp("2012-12-31 23:57:07.200000"),
                Timestamp("2013-01-01 16:00:00"),
            ),
            Interval(
                Timestamp("2013-01-01 16:00:00"), Timestamp("2013-01-02 08:00:00")
            ),
            Interval(
                Timestamp("2013-01-02 08:00:00"), Timestamp("2013-01-03 00:00:00")
            ),
        ]
    )
).astype(CDT(ordered=True))
tm.assert_series_equal(Series(result), expected)
