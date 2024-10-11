# Extracted from ./data/repos/pandas/pandas/tests/indexes/numeric/test_indexing.py
# GH#7820
result = Index([1, 2, np.nan], dtype=np.float64).get_indexer([np.nan])
expected = np.array([2], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
