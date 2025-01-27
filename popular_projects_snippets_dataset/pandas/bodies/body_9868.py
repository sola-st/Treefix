# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
# GH#6929
ser = Series(np.random.rand(10))
ser_copy = ser.copy()
expected = getattr(ser.rolling(3), method)()
tm.assert_series_equal(ser, ser_copy)
ser = ser + 50000
result = getattr(ser.rolling(3), method)()
tm.assert_series_equal(result, expected)
