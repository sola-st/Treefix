# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_isin.py
# GH48905
mi1 = MultiIndex.from_tuples([(1, nulls_fixture)])
mi2 = MultiIndex.from_tuples([(1, 1), (1, 2)])
result = mi2.isin(mi1)
expected = np.array([False, False])
tm.assert_numpy_array_equal(result, expected)
