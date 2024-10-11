# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
# GH#41934 nans in both index and in target
ii = IntervalIndex.from_breaks(range(5))
ii2 = ii.append(IntervalIndex([np.nan]))
ci2 = CategoricalIndex(ii2)

result = ii2.get_indexer(ci2)
expected = np.arange(5, dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)

# not-all-matches
result = ii2[1:].get_indexer(ci2[::-1])
expected = np.array([3, 2, 1, 0, -1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)

# non-unique target, non-unique nans
result = ii2.get_indexer(ci2.append(ci2))
expected = np.array([0, 1, 2, 3, 4, 0, 1, 2, 3, 4], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
