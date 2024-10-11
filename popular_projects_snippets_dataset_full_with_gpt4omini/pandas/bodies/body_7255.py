# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_join.py
index = Index(range(0, 20, 2), dtype=np.int64)
other = Index([7, 12, 25, 1, 2, 5], dtype=np.int64)
other_mono = Index([1, 2, 5, 7, 12, 25], dtype=np.int64)

# not monotonic
res, lidx, ridx = index.join(other, how="inner", return_indexers=True)

# no guarantee of sortedness, so sort for comparison purposes
ind = res.argsort()
res = res.take(ind)
lidx = lidx.take(ind)
ridx = ridx.take(ind)

eres = Index([2, 12], dtype=np.int64)
elidx = np.array([1, 6], dtype=np.intp)
eridx = np.array([4, 1], dtype=np.intp)

assert isinstance(res, Index) and res.dtype == np.int64
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_numpy_array_equal(ridx, eridx)

# monotonic
res, lidx, ridx = index.join(other_mono, how="inner", return_indexers=True)

res2 = index.intersection(other_mono)
tm.assert_index_equal(res, res2)

elidx = np.array([1, 6], dtype=np.intp)
eridx = np.array([1, 4], dtype=np.intp)
assert isinstance(res, Index) and res.dtype == np.int64
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
tm.assert_numpy_array_equal(ridx, eridx)
