# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_skew_kurt.py
obj = Series(np.random.randn(50))
obj[:10] = np.NaN
obj[-10:] = np.NaN

result = getattr(obj.rolling(20, center=True), roll_func)()
expected = (
    getattr(concat([obj, Series([np.NaN] * 9)]).rolling(20), roll_func)()
    .iloc[9:]
    .reset_index(drop=True)
)
tm.assert_series_equal(result, expected)
