# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH#22533
idx = MultiIndex.from_tuples([(10, 1)])
tm.assert_index_equal(idx[ind1], idx)

expected = MultiIndex(
    levels=[np.array([], dtype=np.int64), np.array([], dtype=np.int64)],
    codes=[[], []],
)
tm.assert_index_equal(idx[ind2], expected)
