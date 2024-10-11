# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
na_value = nulls_fixture
arr = pd.array(["a", pd.NA, "b"], dtype=dtype)
result = arr.to_numpy(na_value=na_value)
expected = np.array(["a", na_value, "b"], dtype=object)
tm.assert_numpy_array_equal(result, expected)
