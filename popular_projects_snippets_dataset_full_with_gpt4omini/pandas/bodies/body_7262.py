# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_join.py
other = Index(2**63 + np.array([7, 12, 25, 1, 2, 10], dtype="uint64"))
other_mono = Index(2**63 + np.array([1, 2, 7, 10, 12, 25], dtype="uint64"))

# not monotonic
res, lidx, ridx = index_large.join(other, how="left", return_indexers=True)
eres = index_large
eridx = np.array([-1, 5, -1, -1, 2], dtype=np.intp)

assert isinstance(res, Index) and res.dtype == np.uint64
tm.assert_index_equal(res, eres)
assert lidx is None
tm.assert_numpy_array_equal(ridx, eridx)

# monotonic
res, lidx, ridx = index_large.join(other_mono, how="left", return_indexers=True)
eridx = np.array([-1, 3, -1, -1, 5], dtype=np.intp)

assert isinstance(res, Index) and res.dtype == np.uint64
tm.assert_index_equal(res, eres)
assert lidx is None
tm.assert_numpy_array_equal(ridx, eridx)

# non-unique
idx = Index(2**63 + np.array([1, 1, 2, 5], dtype="uint64"))
idx2 = Index(2**63 + np.array([1, 2, 5, 7, 9], dtype="uint64"))
res, lidx, ridx = idx2.join(idx, how="left", return_indexers=True)

# 1 is in idx2, so it should be x2
eres = Index(2**63 + np.array([1, 1, 2, 5, 7, 9], dtype="uint64"))
eridx = np.array([0, 1, 2, 3, -1, -1], dtype=np.intp)
elidx = np.array([0, 0, 1, 2, 3, 4], dtype=np.intp)

tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_numpy_array_equal(ridx, eridx)
