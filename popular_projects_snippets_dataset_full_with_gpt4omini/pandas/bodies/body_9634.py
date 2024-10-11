# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_numpy.py
ser = pd.Series([1, 2, 3])
ser.array[0] = 10
expected = pd.Series([10, 2, 3])
tm.assert_series_equal(ser, expected)
