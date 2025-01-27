# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_join.py
index = Index(range(0, 20, 2), dtype=np.int64)
other = Index([7, 12, 25, 1, 2, 5], dtype=np.int64)
other_mono = Index([1, 2, 5, 7, 12, 25], dtype=np.int64)

# not monotonic
res, lidx, ridx = index.join(other, how="right", return_indexers=True)
eres = other
elidx = np.array([-1, 6, -1, -1, 1, -1], dtype=np.intp)

assert isinstance(other, Index) and other.dtype == np.int64
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
assert ridx is None

# monotonic
res, lidx, ridx = index.join(other_mono, how="right", return_indexers=True)
eres = other_mono
elidx = np.array([-1, 1, -1, -1, 6, -1], dtype=np.intp)
assert isinstance(other, Index) and other.dtype == np.int64
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
assert ridx is None

# non-unique
idx = Index([1, 1, 2, 5])
idx2 = Index([1, 2, 5, 7, 9])
res, lidx, ridx = idx.join(idx2, how="right", return_indexers=True)
eres = Index([1, 1, 2, 5, 7, 9])  # 1 is in idx2, so it should be x2
elidx = np.array([0, 1, 2, 3, -1, -1], dtype=np.intp)
eridx = np.array([0, 0, 1, 2, 3, 4], dtype=np.intp)
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_numpy_array_equal(ridx, eridx)
