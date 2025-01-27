# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
N = 127
arr = np.arange(N).astype(dtype)
values = np.arange(N).astype(dtype)
arr.flags.writeable = writable
values.flags.writeable = writable
result = ht.ismember(arr, values)
expected = np.ones_like(values, dtype=np.bool_)
tm.assert_numpy_array_equal(result, expected)
