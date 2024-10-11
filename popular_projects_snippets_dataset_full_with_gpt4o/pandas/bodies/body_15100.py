# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
# This shouldn't produce a warning.
ser = Series(date_range("2000", periods=2))
expected = np.array(["2000-01-01", "2000-01-02"], dtype="M8[ns]")
result = np.asarray(ser)

tm.assert_numpy_array_equal(result, expected)
