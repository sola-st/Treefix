# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_to_numpy.py
# array with both NaN and NA -> only fill NA with `na_value`
arr = FloatingArray(np.array([0.0, np.nan, 0.0]), np.array([False, False, True]))
result = arr.to_numpy(dtype="float64", na_value=-1)
expected = np.array([0.0, np.nan, -1.0], dtype="float64")
tm.assert_numpy_array_equal(result, expected)
