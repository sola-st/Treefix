# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
# GH12679
values = np.array([2, 1, 5, 22, 3, -1, 8]).astype(dtype)
values.flags.writeable = writable
keys, counts = ht.value_count(values, False)
tm.assert_numpy_array_equal(keys, values)
assert np.all(counts == 1)
