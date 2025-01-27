# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_join.py
other = Index(2**63 + np.array([7, 12, 25, 1, 2, 10], dtype="uint64"))
other_mono = Index(2**63 + np.array([1, 2, 7, 10, 12, 25], dtype="uint64"))

# not monotonic
res, lidx, ridx = index_large.join(other, how="right", return_indexers=True)
eres = other
elidx = np.array([-1, -1, 4, -1, -1, 1], dtype=np.intp)

tm.assert_numpy_array_equal(lidx, elidx)
assert isinstance(other, Index) and other.dtype == np.uint64
tm.assert_index_equal(res, eres)
assert ridx is None

# monotonic
res, lidx, ridx = index_large.join(
    other_mono, how="right", return_indexers=True
)
eres = other_mono
elidx = np.array([-1, -1, -1, 1, -1, 4], dtype=np.intp)

assert isinstance(other, Index) and other.dtype == np.uint64
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_index_equal(res, eres)
assert ridx is None

# non-unique
idx = Index(2**63 + np.array([1, 1, 2, 5], dtype="uint64"))
idx2 = Index(2**63 + np.array([1, 2, 5, 7, 9], dtype="uint64"))
res, lidx, ridx = idx.join(idx2, how="right", return_indexers=True)

# 1 is in idx2, so it should be x2
eres = Index(2**63 + np.array([1, 1, 2, 5, 7, 9], dtype="uint64"))
elidx = np.array([0, 1, 2, 3, -1, -1], dtype=np.intp)
eridx = np.array([0, 0, 1, 2, 3, 4], dtype=np.intp)

tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_numpy_array_equal(ridx, eridx)
