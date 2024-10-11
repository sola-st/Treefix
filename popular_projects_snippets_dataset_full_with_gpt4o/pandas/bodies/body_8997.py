# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_array.py
# GH 13853 make sure ufunc is applied to fill_value, including its arg
sparse = SparseArray([1, np.nan, 2, np.nan, -2])
result = SparseArray([2, np.nan, 3, np.nan, -1])
tm.assert_sp_array_equal(np.add(sparse, 1), result)

sparse = SparseArray([1, -1, 2, -2], fill_value=1)
result = SparseArray([2, 0, 3, -1], fill_value=2)
tm.assert_sp_array_equal(np.add(sparse, 1), result)

sparse = SparseArray([1, -1, 0, -2], fill_value=0)
result = SparseArray([2, 0, 1, -1], fill_value=1)
tm.assert_sp_array_equal(np.add(sparse, 1), result)
