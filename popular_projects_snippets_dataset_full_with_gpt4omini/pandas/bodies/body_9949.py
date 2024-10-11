# Extracted from ./data/repos/pandas/pandas/tests/window/test_expanding.py
ser = Series(np.random.randn(50))

result = getattr(ser.expanding(min_periods=30, axis=0), func)()
assert result[:29].isna().all()
tm.assert_almost_equal(result.iloc[-1], static_comp(ser[:50]))

# min_periods is working correctly
result = getattr(ser.expanding(min_periods=15, axis=0), func)()
assert isna(result.iloc[13])
assert notna(result.iloc[14])

ser2 = Series(np.random.randn(20))
result = getattr(ser2.expanding(min_periods=5, axis=0), func)()
assert isna(result[3])
assert notna(result[4])

# min_periods=0
result0 = getattr(ser.expanding(min_periods=0, axis=0), func)()
result1 = getattr(ser.expanding(min_periods=1, axis=0), func)()
tm.assert_almost_equal(result0, result1)

result = getattr(ser.expanding(min_periods=1, axis=0), func)()
tm.assert_almost_equal(result.iloc[-1], static_comp(ser[:50]))
