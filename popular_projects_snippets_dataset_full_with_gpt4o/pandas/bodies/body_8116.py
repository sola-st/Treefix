# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
mi = MultiIndex.from_tuples([(1, 2), (4, 5), (8, 9)])
index = Index(["foo", "bar", "baz"])

result = mi == index
expected = np.array([False, False, False])
tm.assert_numpy_array_equal(result, expected)
