# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
values = np.array([np.nan, np.nan, np.nan], dtype=dtype)
result = ht.duplicated(values)
expected = np.array([False, True, True])
tm.assert_numpy_array_equal(result, expected)
