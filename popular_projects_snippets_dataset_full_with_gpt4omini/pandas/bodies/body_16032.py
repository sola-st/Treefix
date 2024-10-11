# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_describe.py
name = tz = "CET"
start = Timestamp(2018, 1, 1)
end = Timestamp(2018, 1, 5)
s = Series(date_range(start, end, tz=tz), name=name)

result = s.describe()

expected = Series(
    [
        5,
        Timestamp("2018-01-03 00:00:00", tz=tz),
        Timestamp("2018-01-01 00:00:00", tz=tz),
        Timestamp("2018-01-02 00:00:00", tz=tz),
        Timestamp("2018-01-03 00:00:00", tz=tz),
        Timestamp("2018-01-04 00:00:00", tz=tz),
        Timestamp("2018-01-05 00:00:00", tz=tz),
    ],
    name=name,
    index=["count", "mean", "min", "25%", "50%", "75%", "max"],
)
tm.assert_series_equal(result, expected)
