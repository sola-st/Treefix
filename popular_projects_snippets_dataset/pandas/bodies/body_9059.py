# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_constructors.py
result = SparseArray([1, 0, 0, 1], dtype="Sparse[int32]")
expected = SparseArray([1, 0, 0, 1], dtype=np.int32)
tm.assert_sp_array_equal(result, expected)
assert result.sp_values.dtype == np.dtype("int32")
