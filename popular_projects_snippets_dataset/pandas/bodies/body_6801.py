# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
# GH 30063: categorical and non-categorical results should be consistent
index = IntervalIndex.from_tuples([(0, 1), (1, 2), (3, 4)])
categorical_target = CategoricalIndex(target, ordered=ordered)

result = index.get_indexer(categorical_target)
expected = index.get_indexer(target)
tm.assert_numpy_array_equal(result, expected)
