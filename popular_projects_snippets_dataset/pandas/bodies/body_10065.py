# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_functions.py
obj = Series(np.random.randn(50))
obj[:10] = np.NaN
obj[-10:] = np.NaN
result = obj.rolling(50, min_periods=30).count()
tm.assert_almost_equal(
    result.iloc[-1], np.isfinite(obj[10:-10]).astype(float).sum()
)
