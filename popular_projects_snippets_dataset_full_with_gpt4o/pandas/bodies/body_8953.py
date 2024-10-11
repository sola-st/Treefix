# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_unary.py
arr = SparseArray([-1, -2, np.nan, 3], fill_value=np.nan, dtype=np.int8)
res = abs(arr)
exp = SparseArray([1, 2, np.nan, 3], fill_value=np.nan, dtype=np.int8)
tm.assert_sp_array_equal(exp, res)

arr = SparseArray([-1, -2, 1, 3], fill_value=-1, dtype=np.int8)
res = abs(arr)
exp = SparseArray([1, 2, 1, 3], fill_value=1, dtype=np.int8)
tm.assert_sp_array_equal(exp, res)
