# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_join.py
other = Index(2**63 + np.array([7, 12, 25, 1, 2, 10], dtype="uint64"))
other_mono = Index(2**63 + np.array([1, 2, 7, 10, 12, 25], dtype="uint64"))

# not monotonic
# guarantee of sortedness
res, lidx, ridx = index_large.join(other, how="outer", return_indexers=True)
noidx_res = index_large.join(other, how="outer")
tm.assert_index_equal(res, noidx_res)

eres = Index(
    2**63 + np.array([0, 1, 2, 7, 10, 12, 15, 20, 25], dtype="uint64")
)
elidx = np.array([0, -1, -1, -1, 1, -1, 2, 3, 4], dtype=np.intp)
eridx = np.array([-1, 3, 4, 0, 5, 1, -1, -1, 2], dtype=np.intp)

assert isinstance(res, Index) and res.dtype == np.uint64
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_numpy_array_equal(ridx, eridx)

# monotonic
res, lidx, ridx = index_large.join(
    other_mono, how="outer", return_indexers=True
)
noidx_res = index_large.join(other_mono, how="outer")
tm.assert_index_equal(res, noidx_res)

elidx = np.array([0, -1, -1, -1, 1, -1, 2, 3, 4], dtype=np.intp)
eridx = np.array([-1, 0, 1, 2, 3, 4, -1, -1, 5], dtype=np.intp)

assert isinstance(res, Index) and res.dtype == np.uint64
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_numpy_array_equal(ridx, eridx)
