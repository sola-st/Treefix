# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_libsparse.py
idx = make_sparse_index(4, np.array([2, 3], dtype=np.int32), kind=kind)

res = idx.lookup_array(np.array([-1, 0, 2], dtype=np.int32))
exp = np.array([-1, -1, 0], dtype=np.int32)
tm.assert_numpy_array_equal(res, exp)

res = idx.lookup_array(np.array([4, 2, 1, 3], dtype=np.int32))
exp = np.array([-1, 0, -1, 1], dtype=np.int32)
tm.assert_numpy_array_equal(res, exp)

idx = make_sparse_index(4, np.array([], dtype=np.int32), kind=kind)
res = idx.lookup_array(np.array([-1, 0, 2, 4], dtype=np.int32))
exp = np.array([-1, -1, -1, -1], dtype=np.int32)
tm.assert_numpy_array_equal(res, exp)

idx = make_sparse_index(4, np.array([0, 1, 2, 3], dtype=np.int32), kind=kind)
res = idx.lookup_array(np.array([-1, 0, 2], dtype=np.int32))
exp = np.array([-1, 0, 2], dtype=np.int32)
tm.assert_numpy_array_equal(res, exp)

res = idx.lookup_array(np.array([4, 2, 1, 3], dtype=np.int32))
exp = np.array([-1, 2, 1, 3], dtype=np.int32)
tm.assert_numpy_array_equal(res, exp)

idx = make_sparse_index(4, np.array([0, 2, 3], dtype=np.int32), kind=kind)
res = idx.lookup_array(np.array([2, 1, 3, 0], dtype=np.int32))
exp = np.array([1, -1, 2, 0], dtype=np.int32)
tm.assert_numpy_array_equal(res, exp)

res = idx.lookup_array(np.array([1, 4, 2, 5], dtype=np.int32))
exp = np.array([-1, -1, 1, -1], dtype=np.int32)
tm.assert_numpy_array_equal(res, exp)
