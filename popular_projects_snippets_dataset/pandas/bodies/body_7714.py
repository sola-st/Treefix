# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_equivalence.py
# GH#34180

mi = MultiIndex.from_tuples([("a", "b"), ("b", "c"), ("c", "a")])

result = mi == ("c", "a")
expected = np.array([False, False, True])
tm.assert_numpy_array_equal(result, expected)

result = mi == ("c",)
expected = np.array([False, False, False])
tm.assert_numpy_array_equal(result, expected)
