# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_indexing.py
# GH 23122
spar_bool = SparseArray([False, True] * 5, dtype=np.bool_, fill_value=True)
exp = SparseArray([np.nan, 2, np.nan, 5, 6])
tm.assert_sp_array_equal(arr[spar_bool], exp)

spar_bool = ~spar_bool
res = arr[spar_bool]
exp = SparseArray([np.nan, 1, 3, 4, np.nan])
tm.assert_sp_array_equal(res, exp)

spar_bool = SparseArray(
    [False, True, np.nan] * 3, dtype=np.bool_, fill_value=np.nan
)
res = arr[spar_bool]
exp = SparseArray([np.nan, 3, 5])
tm.assert_sp_array_equal(res, exp)
