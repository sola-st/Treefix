# Extracted from ./data/repos/pandas/pandas/tests/window/test_apply.py
obj = Series(np.random.randn(50))
obj[:10] = np.NaN
obj[-10:] = np.NaN

result = obj.rolling(20, min_periods=15, center=True).apply(f, raw=raw)
expected = (
    concat([obj, Series([np.NaN] * 9)])
    .rolling(20, min_periods=15)
    .apply(f, raw=raw)
    .iloc[9:]
    .reset_index(drop=True)
)
tm.assert_series_equal(result, expected)
