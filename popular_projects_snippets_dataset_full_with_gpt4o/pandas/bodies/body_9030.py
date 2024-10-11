# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_libsparse.py
idx = make_sparse_index(4, np.array([2, 3], dtype=np.int32), kind="integer")
assert isinstance(idx, IntIndex)
assert idx.npoints == 2
tm.assert_numpy_array_equal(idx.indices, np.array([2, 3], dtype=np.int32))

idx = make_sparse_index(4, np.array([], dtype=np.int32), kind="integer")
assert isinstance(idx, IntIndex)
assert idx.npoints == 0
tm.assert_numpy_array_equal(idx.indices, np.array([], dtype=np.int32))

idx = make_sparse_index(
    4, np.array([0, 1, 2, 3], dtype=np.int32), kind="integer"
)
assert isinstance(idx, IntIndex)
assert idx.npoints == 4
tm.assert_numpy_array_equal(idx.indices, np.array([0, 1, 2, 3], dtype=np.int32))
