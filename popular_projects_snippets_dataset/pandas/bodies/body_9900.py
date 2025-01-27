# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_quantile.py
compare_func = partial(scoreatpercentile, per=q)
obj = Series(np.random.randn(50))
obj[:10] = np.NaN
obj[-10:] = np.NaN

result = obj.rolling(50, min_periods=30).quantile(q)
tm.assert_almost_equal(result.iloc[-1], compare_func(obj[10:-10]))

# min_periods is working correctly
result = obj.rolling(20, min_periods=15).quantile(q)
assert isna(result.iloc[23])
assert not isna(result.iloc[24])

assert not isna(result.iloc[-6])
assert isna(result.iloc[-5])

obj2 = Series(np.random.randn(20))
result = obj2.rolling(10, min_periods=5).quantile(q)
assert isna(result.iloc[3])
assert notna(result.iloc[4])

result0 = obj.rolling(20, min_periods=0).quantile(q)
result1 = obj.rolling(20, min_periods=1).quantile(q)
tm.assert_almost_equal(result0, result1)
