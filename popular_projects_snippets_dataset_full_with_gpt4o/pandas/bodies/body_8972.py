# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_astype.py
a = SparseArray([1, 0, 0, 1], dtype=SparseDtype(int, 0))
result = a.astype(bool)
expected = np.array([1, 0, 0, 1], dtype=bool)
tm.assert_numpy_array_equal(result, expected)

# update fill value
result = a.astype(SparseDtype(bool, False))
expected = SparseArray(
    [True, False, False, True], dtype=SparseDtype(bool, False)
)
tm.assert_sp_array_equal(result, expected)
