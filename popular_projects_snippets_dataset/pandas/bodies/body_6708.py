# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_tree.py
left, right = np.array([0, 2], dtype=dtype), np.array([1, 3], dtype=dtype)
tree = IntervalTree(left, right)
target = np.array([target_value], dtype=target_dtype)

result_indexer, result_missing = tree.get_indexer_non_unique(target)
expected_indexer = np.array([-1], dtype="intp")
tm.assert_numpy_array_equal(result_indexer, expected_indexer)

expected_missing = np.array([0], dtype="intp")
tm.assert_numpy_array_equal(result_missing, expected_missing)
