# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_join.py
other = Index(2**63 + np.array([7, 12, 25, 1, 2, 10], dtype="uint64"))
other_mono = Index(2**63 + np.array([1, 2, 7, 10, 12, 25], dtype="uint64"))

# not monotonic
res, lidx, ridx = index_large.join(other, how="inner", return_indexers=True)

# no guarantee of sortedness, so sort for comparison purposes
ind = res.argsort()
res = res.take(ind)
lidx = lidx.take(ind)
ridx = ridx.take(ind)

eres = Index(2**63 + np.array([10, 25], dtype="uint64"))
elidx = np.array([1, 4], dtype=np.intp)
eridx = np.array([5, 2], dtype=np.intp)

assert isinstance(res, Index) and res.dtype == np.uint64
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_numpy_array_equal(ridx, eridx)

# monotonic
res, lidx, ridx = index_large.join(
    other_mono, how="inner", return_indexers=True
)

res2 = index_large.intersection(other_mono)
tm.assert_index_equal(res, res2)

elidx = np.array([1, 4], dtype=np.intp)
eridx = np.array([3, 5], dtype=np.intp)

assert isinstance(res, Index) and res.dtype == np.uint64
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_numpy_array_equal(ridx, eridx)
