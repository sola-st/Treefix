# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_indexing.py
# https://github.com/pandas-dev/pandas/issues/19551
ci = CategoricalIndex(["a", "b"], categories=["a", "b"])

result = ci.get_indexer(CategoricalIndex(["b", "b"], categories=["b", "a"]))
expected = np.array([1, 1], dtype="intp")
tm.assert_numpy_array_equal(result, expected)
