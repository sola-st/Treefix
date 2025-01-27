# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
table = ht.Int64HashTable()
vals = np.array([1, 2, -1, 2, 1, -1], dtype=np.int64)
vals.flags.writeable = writable
arr, unique = table.get_labels_groupby(vals)
expected_arr = np.array([0, 1, -1, 1, 0, -1], dtype=np.intp)
expected_unique = np.array([1, 2], dtype=np.int64)
tm.assert_numpy_array_equal(arr, expected_arr)
tm.assert_numpy_array_equal(unique, expected_unique)
