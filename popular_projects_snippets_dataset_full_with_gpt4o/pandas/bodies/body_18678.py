# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
values = np.array([2, 1, 5, 22, 3, -1, 8]).astype(dtype)
values.flags.writeable = writable
keys = ht.mode(values, False)
tm.assert_numpy_array_equal(keys, values)
