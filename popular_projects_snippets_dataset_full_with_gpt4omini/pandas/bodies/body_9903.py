# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_quantile.py
# shifter index
s = [f"x{x:d}" for x in range(12)]

series_xp = (
    series.reindex(list(series.index) + s)
    .rolling(window=25)
    .quantile(q)
    .shift(-12)
    .reindex(series.index)
)

series_rs = series.rolling(window=25, center=True).quantile(q)
tm.assert_series_equal(series_xp, series_rs)
