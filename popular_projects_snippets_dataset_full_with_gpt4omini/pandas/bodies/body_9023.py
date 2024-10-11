# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_libsparse.py
idx = make_sparse_index(4, np.array([2, 3], dtype=np.int32), kind="block")
assert isinstance(idx, BlockIndex)
assert idx.npoints == 2
tm.assert_numpy_array_equal(idx.blocs, np.array([2], dtype=np.int32))
tm.assert_numpy_array_equal(idx.blengths, np.array([2], dtype=np.int32))

idx = make_sparse_index(4, np.array([], dtype=np.int32), kind="block")
assert isinstance(idx, BlockIndex)
assert idx.npoints == 0
tm.assert_numpy_array_equal(idx.blocs, np.array([], dtype=np.int32))
tm.assert_numpy_array_equal(idx.blengths, np.array([], dtype=np.int32))

idx = make_sparse_index(4, np.array([0, 1, 2, 3], dtype=np.int32), kind="block")
assert isinstance(idx, BlockIndex)
assert idx.npoints == 4
tm.assert_numpy_array_equal(idx.blocs, np.array([0], dtype=np.int32))
tm.assert_numpy_array_equal(idx.blengths, np.array([4], dtype=np.int32))

idx = make_sparse_index(4, np.array([0, 2, 3], dtype=np.int32), kind="block")
assert isinstance(idx, BlockIndex)
assert idx.npoints == 3
tm.assert_numpy_array_equal(idx.blocs, np.array([0, 2], dtype=np.int32))
tm.assert_numpy_array_equal(idx.blengths, np.array([1, 2], dtype=np.int32))
