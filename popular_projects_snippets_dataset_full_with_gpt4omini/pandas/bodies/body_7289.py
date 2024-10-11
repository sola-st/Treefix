# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_astype.py
obj = timedelta_range("1H", periods=2)
result = obj.astype(bool)
expected = Index(np.array([True, True]))
tm.assert_index_equal(result, expected)

result = obj._data.astype(bool)
expected = np.array([True, True])
tm.assert_numpy_array_equal(result, expected)
