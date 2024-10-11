# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
N = 43
expected = (np.arange(N) + N).astype(dtype)
values = np.repeat(expected, 5)
values.flags.writeable = writable
keys, counts = ht.value_count(values, False)
tm.assert_numpy_array_equal(np.sort(keys), expected)
assert np.all(counts == 5)
