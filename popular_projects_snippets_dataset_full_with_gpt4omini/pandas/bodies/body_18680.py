# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
keys = np.array([1, 2, 2, 2, 1, 3], dtype=np.intp)
keys.flags.writeable = writable
result = ht.unique_label_indices(keys)
expected = np.array([0, 1, 5], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
