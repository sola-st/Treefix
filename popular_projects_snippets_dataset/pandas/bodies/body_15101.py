# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
tz = "US/Central"
ser = Series(date_range("2000", periods=2, tz=tz))
expected = np.array(["2000-01-01T06", "2000-01-02T06"], dtype="M8[ns]")
result = np.asarray(ser, dtype="datetime64[ns]")

tm.assert_numpy_array_equal(result, expected)

# Old behavior with no warning
result = np.asarray(ser, dtype="M8[ns]")

tm.assert_numpy_array_equal(result, expected)
