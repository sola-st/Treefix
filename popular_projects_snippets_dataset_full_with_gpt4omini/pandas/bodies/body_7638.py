# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_drop.py
# GH#33494
mi = MultiIndex.from_tuples([(1, 2), (2, 3), (1, 2)])
with warnings.catch_warnings():
    warnings.simplefilter("ignore", PerformanceWarning)
    result = mi.drop((1, 2))
expected = MultiIndex.from_tuples([(2, 3)])
tm.assert_index_equal(result, expected)
