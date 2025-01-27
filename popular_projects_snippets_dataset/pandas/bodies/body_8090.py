# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
# see gh-16991
index = Index(["a", "b"])
expected = np.array([False, False])

result = index.isin(empty)
tm.assert_numpy_array_equal(expected, result)
