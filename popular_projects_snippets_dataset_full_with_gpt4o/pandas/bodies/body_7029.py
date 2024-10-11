# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_indexing.py
arr = np.array(
    [Timestamp("1999-12-31 00:00:00"), Timestamp("2000-12-31 00:00:00")],
    dtype=object,
)
cats = [Timestamp("1999-12-31 00:00:00"), Timestamp("2000-12-31 00:00:00")]
ci = CategoricalIndex(cats, categories=cats, ordered=False, dtype="category")
result = ci.get_indexer(arr)
expected = np.array([0, 1], dtype="intp")
tm.assert_numpy_array_equal(result, expected)
