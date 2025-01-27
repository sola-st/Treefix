# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
# see gh-16991
vals = Index(["a", "b"])
expected = np.array([False, False])

result = algos.isin(vals, empty)
tm.assert_numpy_array_equal(expected, result)
