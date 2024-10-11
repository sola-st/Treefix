# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
N = 17
arr = np.arange(N).astype(dtype)
values = (np.arange(N) + N).astype(dtype)
result = ht.ismember(arr, values)
expected = np.zeros_like(values, dtype=np.bool_)
tm.assert_numpy_array_equal(result, expected)
