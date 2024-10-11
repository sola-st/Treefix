# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_setops.py
# GH#38743
index = IntervalIndex.from_tuples([(1, 2), (1, 2), (2, 3), (3, 4)])
other = IntervalIndex.from_tuples([(1, 2), (2, 3)])
expected = IntervalIndex.from_tuples([(1, 2), (2, 3)])
result = index.intersection(other)
tm.assert_index_equal(result, expected)
