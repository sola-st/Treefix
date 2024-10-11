# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_constructors.py
arr = SparseArray(data=[1, 2], sparse_index=IntIndex(4, [1, 2]))
# TODO: actionable?
# XXX: Behavior change: specifying SparseIndex no longer changes the
# fill_value
expected = SparseArray([0, 1, 2, 0], kind="integer")
tm.assert_sp_array_equal(arr, expected)
assert arr.dtype == SparseDtype(np.int64)
assert arr.fill_value == 0

arr = SparseArray(
    data=[1, 2, 3],
    sparse_index=IntIndex(4, [1, 2, 3]),
    dtype=np.int64,
    fill_value=0,
)
exp = SparseArray([0, 1, 2, 3], dtype=np.int64, fill_value=0)
tm.assert_sp_array_equal(arr, exp)
assert arr.dtype == SparseDtype(np.int64)
assert arr.fill_value == 0

arr = SparseArray(
    data=[1, 2], sparse_index=IntIndex(4, [1, 2]), fill_value=0, dtype=np.int64
)
exp = SparseArray([0, 1, 2, 0], fill_value=0, dtype=np.int64)
tm.assert_sp_array_equal(arr, exp)
assert arr.dtype == SparseDtype(np.int64)
assert arr.fill_value == 0

arr = SparseArray(
    data=[1, 2, 3],
    sparse_index=IntIndex(4, [1, 2, 3]),
    dtype=None,
    fill_value=0,
)
exp = SparseArray([0, 1, 2, 3], dtype=None)
tm.assert_sp_array_equal(arr, exp)
assert arr.dtype == SparseDtype(np.int64)
assert arr.fill_value == 0
