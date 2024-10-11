# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_indexing.py
# GH 45110
arr = SparseArray([1, 2, 3, 4, np.nan, np.nan], fill_value=np.nan)
res = arr[arr > 2]
exp = SparseArray([3.0, 4.0], fill_value=np.nan)
tm.assert_sp_array_equal(res, exp)
