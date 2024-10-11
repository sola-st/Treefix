# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_tz_localize.py
# Matching the index of the result with that of the original series
# GH 43080
dt_series = Series(
    date_range(start="2021-01-01T02:00:00", periods=5, freq="1D"),
    index=[2, 6, 7, 8, 11],
    dtype="category",
)
result = dt_series.dt.tz_localize("Europe/Berlin")
expected = Series(
    date_range(
        start="2021-01-01T02:00:00", periods=5, freq="1D", tz="Europe/Berlin"
    ),
    index=[2, 6, 7, 8, 11],
)
tm.assert_series_equal(result, expected)
