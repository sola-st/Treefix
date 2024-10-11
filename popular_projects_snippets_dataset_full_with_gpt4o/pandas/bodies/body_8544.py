# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_datetime.py
# This shouldn't produce a warning.
idx = date_range("2000", periods=2)
# M8[ns] by default
result = np.asarray(idx)

expected = np.array(["2000-01-01", "2000-01-02"], dtype="M8[ns]")
tm.assert_numpy_array_equal(result, expected)

# optionally, object
result = np.asarray(idx, dtype=object)

expected = np.array([Timestamp("2000-01-01"), Timestamp("2000-01-02")])
tm.assert_numpy_array_equal(result, expected)
