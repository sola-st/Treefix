# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
# Tests regression #21172.
sa = SparseArray([float("nan"), float("nan"), 1, 0, 0, 2, 0, 0, 0, 3, 0, 0])
expected = np.array([2, 5, 9], dtype=np.int32)
(result,) = sa.nonzero()
tm.assert_numpy_array_equal(expected, result)

sa = SparseArray([0, 0, 1, 0, 0, 2, 0, 0, 0, 3, 0, 0])
(result,) = sa.nonzero()
tm.assert_numpy_array_equal(expected, result)
