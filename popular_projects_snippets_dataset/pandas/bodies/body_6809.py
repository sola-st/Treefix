# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
# GH#44084 (MultiIndex case as reported)
interval_index = IntervalIndex.from_tuples(
    [(2.0, 3.0), (0.0, 1.0), (1.0, 2.0)], name="interval"
)
foo_index = Index([1, 2, 3], name="foo")

multi_index = MultiIndex.from_product([foo_index, interval_index])

result = multi_index.get_level_values("interval").get_indexer_for(
    [Interval(0.0, 1.0)]
)
expected = np.array([1, 4, 7], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
