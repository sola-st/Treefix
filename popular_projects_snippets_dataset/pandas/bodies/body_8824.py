# Extracted from ./data/repos/pandas/pandas/tests/arrays/string_/test_string.py
vals = ["a", "b", "c"]
arr = np.array(vals, dtype=np.str_)
result = pd.array(arr, dtype=dtype)
expected = pd.array(vals, dtype=dtype)
tm.assert_extension_array_equal(result, expected)
