# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
arr = np.array([np.nan, np.nan, np.nan], dtype=dtype)
values = np.array([1], dtype=dtype)
result = ht.ismember(arr, values)
expected = np.array([False, False, False], dtype=np.bool_)
tm.assert_numpy_array_equal(result, expected)
