# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
keys = [[np.nan] * 5 + list(range(100)) + [np.nan] * 5]
result = lexsort_indexer(keys, orders=order, na_position=na_position)
tm.assert_numpy_array_equal(result, np.array(exp, dtype=np.intp))
