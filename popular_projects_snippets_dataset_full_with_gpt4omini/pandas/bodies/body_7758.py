# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_indexing.py
# GH#48411
idx = Index([1, 2, NA, NA], dtype="Int64")
result = idx.get_loc(NA)
expected = np.array([False, False, True, True])
tm.assert_numpy_array_equal(result, expected)
