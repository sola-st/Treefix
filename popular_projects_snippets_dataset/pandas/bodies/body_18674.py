# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
N = 100
values = np.repeat(np.arange(N).astype(dtype), 5)
values.flags.writeable = writable
result = ht.duplicated(values)
expected = np.ones_like(values, dtype=np.bool_)
expected[::5] = False
tm.assert_numpy_array_equal(result, expected)
