# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_interval_tree.py
x = np.arange(1000, dtype="float64")
found = x.astype("intp")
not_found = (-1 * np.ones(1000)).astype("intp")

tree = IntervalTree(x, x + 0.5, closed=closed, leaf_size=leaf_size)
tm.assert_numpy_array_equal(found, tree.get_indexer(x + 0.25))

expected = found if tree.closed_left else not_found
tm.assert_numpy_array_equal(expected, tree.get_indexer(x + 0.0))

expected = found if tree.closed_right else not_found
tm.assert_numpy_array_equal(expected, tree.get_indexer(x + 0.5))
