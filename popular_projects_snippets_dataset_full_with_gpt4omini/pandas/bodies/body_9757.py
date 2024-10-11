# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_skew_kurt.py
# shifter index
s = [f"x{x:d}" for x in range(12)]

series_xp = (
    getattr(
        series.reindex(list(series.index) + s).rolling(window=25),
        roll_func,
    )()
    .shift(-12)
    .reindex(series.index)
)
series_rs = getattr(series.rolling(window=25, center=True), roll_func)()
tm.assert_series_equal(series_xp, series_rs)
