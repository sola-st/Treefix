# Extracted from ./data/repos/pandas/pandas/tests/arrays/integer/test_indexing.py
# GH 31446
arr = pd.Series([1, 2], dtype="Int64").array
arr[arr > 1] = 1

expected = pd.array([1, 1], dtype="Int64")
tm.assert_extension_array_equal(arr, expected)
