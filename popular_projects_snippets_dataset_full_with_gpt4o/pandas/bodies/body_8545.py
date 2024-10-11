# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_datetime.py
tz = "US/Central"
idx = date_range("2000", periods=2, tz=tz)
expected = np.array(["2000-01-01T06", "2000-01-02T06"], dtype="M8[ns]")
result = np.asarray(idx, dtype="datetime64[ns]")

tm.assert_numpy_array_equal(result, expected)

# Old behavior with no warning
result = np.asarray(idx, dtype="M8[ns]")

tm.assert_numpy_array_equal(result, expected)

# Future behavior with no warning
expected = np.array(
    [Timestamp("2000-01-01", tz=tz), Timestamp("2000-01-02", tz=tz)]
)
result = np.asarray(idx, dtype=object)

tm.assert_numpy_array_equal(result, expected)
