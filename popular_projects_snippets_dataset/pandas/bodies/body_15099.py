# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
ser = Series(date_range("2000", periods=2, tz=tz))

with tm.assert_produces_warning(None):
    # Future behavior (for tzaware case) with no warning
    result = np.asarray(ser, dtype=object)

expected = np.array(
    [Timestamp("2000-01-01", tz=tz), Timestamp("2000-01-02", tz=tz)]
)
tm.assert_numpy_array_equal(result, expected)
