# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_unary.py
arr = SparseArray([False, True, False, True], fill_value=False, dtype=np.bool_)
exp = SparseArray(
    np.invert([False, True, False, True]), fill_value=True, dtype=np.bool_
)
res = ~arr
tm.assert_sp_array_equal(exp, res)

arr = SparseArray([0, 1, 0, 2, 3, 0], fill_value=0, dtype=np.int32)
res = ~arr
exp = SparseArray([-1, -2, -1, -3, -4, -1], fill_value=-1, dtype=np.int32)
tm.assert_sp_array_equal(exp, res)
