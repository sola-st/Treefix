# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_join.py
# Join with Index[int64]
index = RangeIndex(start=0, stop=20, step=2)
other = Index(np.arange(25, 14, -1, dtype=np.int64))

res, lidx, ridx = index.join(other, how="right", return_indexers=True)
eres = other
elidx = np.array([-1, -1, -1, -1, -1, -1, -1, 9, -1, 8, -1], dtype=np.intp)

assert isinstance(other, Index) and other.dtype == np.int64
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
assert ridx is None

# Join withRangeIndex
other = RangeIndex(25, 14, -1)

res, lidx, ridx = index.join(other, how="right", return_indexers=True)
eres = other

assert isinstance(other, RangeIndex)
tm.assert_index_equal(res, eres)
tm.assert_numpy_array_equal(lidx, elidx)
assert ridx is None
