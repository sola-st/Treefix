# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
N = 3
table = table_type()
keys = (np.arange(N) + N).astype(dtype)
keys.flags.writeable = writable
table.map_locations(keys)
result = table.lookup(keys)
expected = np.arange(N)
tm.assert_numpy_array_equal(result.astype(np.int64), expected.astype(np.int64))
