# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_skew_kurt.py
result = getattr(
    series.rolling(len(series) + 1, min_periods=minp, step=step), roll_func
)()
expected = getattr(
    series.rolling(len(series), min_periods=minp, step=step), roll_func
)()
nan_mask = isna(result)
tm.assert_series_equal(nan_mask, isna(expected))

nan_mask = ~nan_mask
tm.assert_almost_equal(result[nan_mask], expected[nan_mask])
