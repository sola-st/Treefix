# Extracted from ./data/repos/pandas/pandas/tests/window/test_apply.py
# shifter index
s = [f"x{x:d}" for x in range(12)]
minp = 10

series_xp = (
    series.reindex(list(series.index) + s)
    .rolling(window=25, min_periods=minp)
    .apply(f, raw=raw)
    .shift(-12)
    .reindex(series.index)
)
series_rs = series.rolling(window=25, min_periods=minp, center=True).apply(
    f, raw=raw
)
tm.assert_series_equal(series_xp, series_rs)
