# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_indexing.py
# time indexing
idx = date_range("2000-01-01", periods=24, freq="H")

result = idx.get_loc(time(12))
expected = np.array([12])
tm.assert_numpy_array_equal(result, expected, check_dtype=False)

result = idx.get_loc(time(12, 30))
expected = np.array([])
tm.assert_numpy_array_equal(result, expected, check_dtype=False)
