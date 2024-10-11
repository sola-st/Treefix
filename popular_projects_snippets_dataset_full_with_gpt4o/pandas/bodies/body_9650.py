# Extracted from ./data/repos/pandas/pandas/tests/arrays/numpy_/test_indexing.py
arr = pd.array([1, 3, 90], dtype=any_real_numpy_dtype)
result = arr.searchsorted([2, 30])
expected = np.array([1, 2], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
