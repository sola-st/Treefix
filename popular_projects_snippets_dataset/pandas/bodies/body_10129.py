# Extracted from ./data/repos/pandas/pandas/tests/window/test_apply.py
obj = Series(np.random.randn(50))
obj[:10] = np.NaN
obj[-10:] = np.NaN

result = obj.rolling(50, min_periods=30).apply(f, raw=raw)
tm.assert_almost_equal(result.iloc[-1], np.mean(obj[10:-10]))

# min_periods is working correctly
result = obj.rolling(20, min_periods=15).apply(f, raw=raw)
assert isna(result.iloc[23])
assert not isna(result.iloc[24])

assert not isna(result.iloc[-6])
assert isna(result.iloc[-5])

obj2 = Series(np.random.randn(20))
result = obj2.rolling(10, min_periods=5).apply(f, raw=raw)
assert isna(result.iloc[3])
assert notna(result.iloc[4])

result0 = obj.rolling(20, min_periods=0).apply(f, raw=raw)
result1 = obj.rolling(20, min_periods=1).apply(f, raw=raw)
tm.assert_almost_equal(result0, result1)
