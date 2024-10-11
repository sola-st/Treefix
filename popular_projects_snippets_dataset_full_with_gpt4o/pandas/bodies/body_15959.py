# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_to_numpy.py
# GH#48951
ser = Series([1, 2, NA, 4])
result = ser.to_numpy(dtype=dtype, na_value=0)
expected = np.array([1, 2, 0, 4], dtype=dtype)
tm.assert_numpy_array_equal(result, expected)
