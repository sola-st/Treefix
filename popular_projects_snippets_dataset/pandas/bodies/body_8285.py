# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_astype.py
obj = date_range("2000", periods=2, tz=tz, name="idx")
result = obj.astype(bool)
expected = Index(np.array([True, True]), name="idx")
tm.assert_index_equal(result, expected)

result = obj._data.astype(bool)
expected = np.array([True, True])
tm.assert_numpy_array_equal(result, expected)
