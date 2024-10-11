# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_join.py
index = Index(range(0, 20, 2), dtype=np.int64)
other = Index([7, 12, 25, 1, 2, 5], dtype=np.int64)
other_mono = Index([1, 2, 5, 7, 12, 25], dtype=np.int64)

# not monotonic
res, lidx, ridx = index.join(other, how="left", return_indexers=True)
eres = index
eridx = np.array([-1, 4, -1, -1, -1, -1, 1, -1, -1, -1], dtype=np.intp)

assert isinstance(res, Index) and res.dtype == np.int64
tm.assert_index_equal(res, eres)
assert lidx is None
tm.assert_numpy_array_equal(ridx, eridx)

# monotonic
res, lidx, ridx = index.join(other_mono, how="left", return_indexers=True)
eridx = np.array([-1, 1, -1, -1, -1, -1, 4, -1, -1, -1], dtype=np.intp)
assert isinstance(res, Index) and res.dtype == np.int64
tm.assert_index_equal(res, eres)
assert lidx is None
tm.assert_numpy_array_equal(ridx, eridx)

# non-unique
idx = Index([1, 1, 2, 5])
idx2 = Index([1, 2, 5, 7, 9])
res, lidx, ridx = idx2.join(idx, how="left", return_indexers=True)
eres = Index([1, 1, 2, 5, 7, 9])  # 1 is in idx2, so it should be x2
eridx = np.array([0, 1, 2, 3, -1, -1], dtype=np.intp)
elidx = np.array([0, 0, 1, 2, 3, 4], dtype=np.intp)
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_numpy_array_equal(ridx, eridx)
