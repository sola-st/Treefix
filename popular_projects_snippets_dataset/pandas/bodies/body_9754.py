# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling_skew_kurt.py
import scipy.stats

compare_func = partial(getattr(scipy.stats, sp_func), bias=False)
obj = Series(np.random.randn(50))
obj[:10] = np.NaN
obj[-10:] = np.NaN

result = getattr(obj.rolling(50, min_periods=30), roll_func)()
tm.assert_almost_equal(result.iloc[-1], compare_func(obj[10:-10]))

# min_periods is working correctly
result = getattr(obj.rolling(20, min_periods=15), roll_func)()
assert isna(result.iloc[23])
assert not isna(result.iloc[24])

assert not isna(result.iloc[-6])
assert isna(result.iloc[-5])

obj2 = Series(np.random.randn(20))
result = getattr(obj2.rolling(10, min_periods=5), roll_func)()
assert isna(result.iloc[3])
assert notna(result.iloc[4])

result0 = getattr(obj.rolling(20, min_periods=0), roll_func)()
result1 = getattr(obj.rolling(20, min_periods=1), roll_func)()
tm.assert_almost_equal(result0, result1)
