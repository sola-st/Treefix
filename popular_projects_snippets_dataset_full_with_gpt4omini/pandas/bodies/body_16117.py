# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
dt_series = Series(
    date_range(start="2021-01-01", periods=5, freq="h"),
    index=[2, 6, 7, 8, 11],
    dtype="category",
)
result = dt_series.dt.hour
expected = Series(
    [0, 1, 2, 3, 4],
    dtype="int32",
    index=[2, 6, 7, 8, 11],
)
tm.assert_series_equal(result, expected)
