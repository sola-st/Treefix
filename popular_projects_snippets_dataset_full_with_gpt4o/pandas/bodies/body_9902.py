# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_quantile.py
obj = Series(np.random.randn(50))
obj[:10] = np.NaN
obj[-10:] = np.NaN

result = obj.rolling(20, center=True).quantile(q)
expected = (
    concat([obj, Series([np.NaN] * 9)])
    .rolling(20)
    .quantile(q)
    .iloc[9:]
    .reset_index(drop=True)
)
tm.assert_series_equal(result, expected)
