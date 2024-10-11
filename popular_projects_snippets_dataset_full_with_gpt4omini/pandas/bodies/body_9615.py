# Extracted from ./data/repos/pandas/pandas/tests/arrays/floating/test_to_numpy.py
con = pd.Series if box else pd.array

arr = con([0.0, 1.0, None], dtype="Float64")
result = arr.to_numpy(dtype=object, na_value=None)
expected = np.array([0.0, 1.0, None], dtype="object")
tm.assert_numpy_array_equal(result, expected)

result = arr.to_numpy(dtype=bool, na_value=False)
expected = np.array([False, True, False], dtype="bool")
tm.assert_numpy_array_equal(result, expected)

result = arr.to_numpy(dtype="int64", na_value=-99)
expected = np.array([0, 1, -99], dtype="int64")
tm.assert_numpy_array_equal(result, expected)
