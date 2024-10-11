# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
# GH 13853 make sure ufunc is applied to fill_value
sparse = SparseArray([1, np.nan, 2, np.nan, -2])
result = SparseArray([1, np.nan, 2, np.nan, 2])
tm.assert_sp_array_equal(abs(sparse), result)
tm.assert_sp_array_equal(np.abs(sparse), result)

sparse = SparseArray([1, -1, 2, -2], fill_value=1)
result = SparseArray([1, 2, 2], sparse_index=sparse.sp_index, fill_value=1)
tm.assert_sp_array_equal(abs(sparse), result)
tm.assert_sp_array_equal(np.abs(sparse), result)

sparse = SparseArray([1, -1, 2, -2], fill_value=-1)
exp = SparseArray([1, 1, 2, 2], fill_value=1)
tm.assert_sp_array_equal(abs(sparse), exp)
tm.assert_sp_array_equal(np.abs(sparse), exp)

sparse = SparseArray([1, np.nan, 2, np.nan, -2])
result = SparseArray(np.sin([1, np.nan, 2, np.nan, -2]))
tm.assert_sp_array_equal(np.sin(sparse), result)

sparse = SparseArray([1, -1, 2, -2], fill_value=1)
result = SparseArray(np.sin([1, -1, 2, -2]), fill_value=np.sin(1))
tm.assert_sp_array_equal(np.sin(sparse), result)

sparse = SparseArray([1, -1, 0, -2], fill_value=0)
result = SparseArray(np.sin([1, -1, 0, -2]), fill_value=np.sin(0))
tm.assert_sp_array_equal(np.sin(sparse), result)
