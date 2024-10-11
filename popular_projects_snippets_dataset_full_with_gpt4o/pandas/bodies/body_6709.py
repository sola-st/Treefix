# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_tree.py
left = np.array([0, 0, 0], dtype=dtype)
tree = IntervalTree(left, left + 1)

with pytest.raises(
    KeyError, match="'indexer does not intersect a unique set of intervals'"
):
    tree.get_indexer(np.array([0.5]))

indexer, missing = tree.get_indexer_non_unique(np.array([0.5]))
result = np.sort(indexer)
expected = np.array([0, 1, 2], dtype="intp")
tm.assert_numpy_array_equal(result, expected)

result = missing
expected = np.array([], dtype="intp")
tm.assert_numpy_array_equal(result, expected)
