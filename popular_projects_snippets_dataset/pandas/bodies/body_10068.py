# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_functions.py
obj = Series(np.random.randn(50))
obj[:10] = np.NaN
obj[-10:] = np.NaN

result = getattr(obj.rolling(20, min_periods=minp, center=True), roll_func)(
    **kwargs
)
expected = (
    getattr(
        concat([obj, Series([np.NaN] * 9)]).rolling(20, min_periods=minp), roll_func
    )(**kwargs)
    .iloc[9:]
    .reset_index(drop=True)
)
tm.assert_series_equal(result, expected)
