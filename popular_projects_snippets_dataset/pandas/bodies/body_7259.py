# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_join.py
index = Index(range(0, 20, 2), dtype=np.int64)
other = Index([7, 12, 25, 1, 2, 5], dtype=np.int64)
other_mono = Index([1, 2, 5, 7, 12, 25], dtype=np.int64)

# not monotonic
# guarantee of sortedness
res, lidx, ridx = index.join(other, how="outer", return_indexers=True)
noidx_res = index.join(other, how="outer")
tm.assert_index_equal(res, noidx_res)

eres = Index([0, 1, 2, 4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 25], dtype=np.int64)
elidx = np.array([0, -1, 1, 2, -1, 3, -1, 4, 5, 6, 7, 8, 9, -1], dtype=np.intp)
eridx = np.array(
    [-1, 3, 4, -1, 5, -1, 0, -1, -1, 1, -1, -1, -1, 2], dtype=np.intp
)

assert isinstance(res, Index) and res.dtype == np.int64
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_numpy_array_equal(ridx, eridx)

# monotonic
res, lidx, ridx = index.join(other_mono, how="outer", return_indexers=True)
noidx_res = index.join(other_mono, how="outer")
tm.assert_index_equal(res, noidx_res)

elidx = np.array([0, -1, 1, 2, -1, 3, -1, 4, 5, 6, 7, 8, 9, -1], dtype=np.intp)
eridx = np.array(
    [-1, 0, 1, -1, 2, -1, 3, -1, -1, 4, -1, -1, -1, 5], dtype=np.intp
)
assert isinstance(res, Index) and res.dtype == np.int64
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_numpy_array_equal(ridx, eridx)
