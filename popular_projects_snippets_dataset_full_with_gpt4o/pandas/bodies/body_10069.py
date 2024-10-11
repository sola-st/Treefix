# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_functions.py
# shifter index
s = [f"x{x:d}" for x in range(12)]

series_xp = (
    getattr(
        series.reindex(list(series.index) + s).rolling(window=25, min_periods=minp),
        roll_func,
    )(**kwargs)
    .shift(-12)
    .reindex(series.index)
)
series_rs = getattr(
    series.rolling(window=25, min_periods=minp, center=True), roll_func
)(**kwargs)
if fill_value is not None:
    series_xp = series_xp.fillna(fill_value)
tm.assert_series_equal(series_xp, series_rs)
