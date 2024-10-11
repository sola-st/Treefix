# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_tree.py
left, right = np.array([0, 1], dtype=dtype), np.array([1, 2], dtype=dtype)
tree = IntervalTree(left, right)

result = tree.get_indexer(np.array([target_value], dtype=target_dtype))
expected = np.array([-1], dtype="intp")
tm.assert_numpy_array_equal(result, expected)
