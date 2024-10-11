# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_describe.py
# GH 21332
tz = tz_naive_fixture
name = str(tz_naive_fixture)
start = Timestamp(2018, 1, 1)
end = Timestamp(2018, 1, 5)
s = Series(date_range(start, end, tz=tz), name=name)
result = s.describe()
expected = Series(
    [
        5,
        Timestamp(2018, 1, 3).tz_localize(tz),
        start.tz_localize(tz),
        s[1],
        s[2],
        s[3],
        end.tz_localize(tz),
    ],
    name=name,
    index=["count", "mean", "min", "25%", "50%", "75%", "max"],
)
tm.assert_series_equal(result, expected)
