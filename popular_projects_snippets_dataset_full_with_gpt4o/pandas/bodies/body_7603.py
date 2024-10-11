# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
# GH#22533
idx = MultiIndex.from_tuples([(10, 1), (20, 2), (30, 3), (40, 4), (50, 5)])
tm.assert_index_equal(idx[ind1], idx)

expected = MultiIndex.from_tuples([(10, 1), (30, 3)])
tm.assert_index_equal(idx[ind2], expected)
