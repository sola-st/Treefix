# Extracted from ./data/repos/pandas/pandas/tests/libs/test_hashtable.py
# GH-41836
values = [("a", float("nan")), ("b", 1)]
comps = [("a", float("nan"))]
result = isin(values, comps)
expected = np.array([True, False], dtype=np.bool_)
tm.assert_numpy_array_equal(result, expected)
