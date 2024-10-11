# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike_/test_sort_values.py
idx = non_monotonic_idx
ordered = idx.sort_values()
assert ordered.is_monotonic_increasing
ordered = idx.sort_values(ascending=False)
assert ordered[::-1].is_monotonic_increasing

ordered, dexer = idx.sort_values(return_indexer=True)
assert ordered.is_monotonic_increasing
tm.assert_numpy_array_equal(dexer, np.array([1, 2, 0], dtype=np.intp))

ordered, dexer = idx.sort_values(return_indexer=True, ascending=False)
assert ordered[::-1].is_monotonic_increasing
tm.assert_numpy_array_equal(dexer, np.array([0, 2, 1], dtype=np.intp))
