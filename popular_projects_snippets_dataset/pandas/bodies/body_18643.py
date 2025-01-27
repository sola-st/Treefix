# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
if dtype in (np.int8, np.uint8):
    N = 88
else:
    N = 1000
table = table_type()
expected = (np.arange(N) + N).astype(dtype)
keys = np.repeat(expected, 5)
keys.flags.writeable = writable
unique = table.unique(keys)
tm.assert_numpy_array_equal(unique, expected)
