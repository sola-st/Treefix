# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_constructors.py
result = SparseArray([1, 0, 0, 1], dtype=SparseDtype("int64", -1))
expected = SparseArray([1, 0, 0, 1], fill_value=-1, dtype=np.int64)
tm.assert_sp_array_equal(result, expected)
assert result.sp_values.dtype == np.dtype("int64")
