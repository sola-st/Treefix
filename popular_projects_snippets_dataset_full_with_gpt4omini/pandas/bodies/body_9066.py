# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_constructors.py
arr = SparseArray(
    data=[1, 2], sparse_index=IntIndex(4, [1, 2]), fill_value=0, dtype=None
)
exp = SparseArray([0, 1, 2, 0], fill_value=0, dtype=None)
tm.assert_sp_array_equal(arr, exp)
assert arr.dtype == SparseDtype(np.int64)
assert arr.fill_value == 0
