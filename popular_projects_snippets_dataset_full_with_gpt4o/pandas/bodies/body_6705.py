# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_tree.py
result = tree.get_indexer(np.array([1.0, 5.5, 6.5]))
expected = np.array([0, 4, -1], dtype="intp")
tm.assert_numpy_array_equal(result, expected)

with pytest.raises(
    KeyError, match="'indexer does not intersect a unique set of intervals'"
):
    tree.get_indexer(np.array([3.0]))
