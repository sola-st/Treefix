# Extracted from ./data/repos/pandas/pandas/tests/indexes/ranges/test_join.py
# Join with Index[int64]
index = RangeIndex(start=0, stop=20, step=2)
other = Index(np.arange(25, 14, -1, dtype=np.int64))

res, lidx, ridx = index.join(other, how="left", return_indexers=True)
eres = index
eridx = np.array([-1, -1, -1, -1, -1, -1, -1, -1, 9, 7], dtype=np.intp)

assert isinstance(res, RangeIndex)
tm.assert_index_equal(res, eres)
assert lidx is None
tm.assert_numpy_array_equal(ridx, eridx)

# Join withRangeIndex
other = Index(np.arange(25, 14, -1, dtype=np.int64))

res, lidx, ridx = index.join(other, how="left", return_indexers=True)

assert isinstance(res, RangeIndex)
tm.assert_index_equal(res, eres)
assert lidx is None
tm.assert_numpy_array_equal(ridx, eridx)
