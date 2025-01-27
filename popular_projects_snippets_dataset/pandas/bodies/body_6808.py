# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_indexing.py
# GH#44084 (root cause)
index = IntervalIndex.from_tuples(
    [(0.0, 1.0), (1.0, 2.0), (0.0, 1.0), (1.0, 2.0)]
)

result, _ = index.get_indexer_non_unique([Interval(1.0, 2.0)])
expected = np.array([1, 3], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
