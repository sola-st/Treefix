# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_indexing.py
cidx = CategoricalIndex(list("abcb"))
result = cidx.get_loc("b")
expected = np.array([False, True, False, True], dtype=bool)
tm.assert_numpy_array_equal(result, expected)
