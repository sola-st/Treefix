# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
arr = np.array([np.nan, np.nan, np.nan], dtype=dtype)
values = np.array([np.nan, np.nan], dtype=dtype)
result = ht.ismember(arr, values)
expected = np.array([True, True, True], dtype=np.bool_)
tm.assert_numpy_array_equal(result, expected)
