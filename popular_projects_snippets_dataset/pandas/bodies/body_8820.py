# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
arr = pd.array(["a", pd.NA, "b"], dtype=dtype)
result = np.array(arr)
expected = np.array(["a", pd.NA, "b"], dtype=object)
tm.assert_numpy_array_equal(result, expected)
