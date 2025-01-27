# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
# GH#41831
index = IntervalIndex([np.nan, np.nan])
other = IntervalIndex([np.nan])

assert not index._index_as_unique

result = index.get_indexer_for(other)
expected = np.array([0, 1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
