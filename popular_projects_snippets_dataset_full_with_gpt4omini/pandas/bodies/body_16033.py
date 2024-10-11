# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_describe.py
s = Series(date_range("2012", periods=3))
result = s.describe()
expected = Series(
    [
        3,
        Timestamp("2012-01-02"),
        Timestamp("2012-01-01"),
        Timestamp("2012-01-01T12:00:00"),
        Timestamp("2012-01-02"),
        Timestamp("2012-01-02T12:00:00"),
        Timestamp("2012-01-03"),
    ],
    index=["count", "mean", "min", "25%", "50%", "75%", "max"],
)
tm.assert_series_equal(result, expected)
