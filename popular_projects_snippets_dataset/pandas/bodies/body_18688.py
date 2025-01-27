# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
values = ["a", 5, 5.0, 5.0 + 0j]
comps = list(range(129))
result = isin(values, comps)
expected = np.array([False, True, True, True], dtype=np.bool_)
tm.assert_numpy_array_equal(result, expected)
