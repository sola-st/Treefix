# Extracted from ./data/repos/pandas/pandas/tests/arrays/boolean/test_indexing.py
arr = pd.array([True, False, None], dtype="boolean")
expected = pd.array([True, None, None], dtype="boolean")
arr[1] = na
tm.assert_extension_array_equal(arr, expected)
