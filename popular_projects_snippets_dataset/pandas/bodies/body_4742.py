# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series(
    ["a", np.nan, "b", True, datetime.today(), "foo", None, 1, 2.0],
    dtype=object,
)
result = ser.str.count("a")
expected = Series([1, np.nan, 0, np.nan, np.nan, 0, np.nan, np.nan, np.nan])
tm.assert_series_equal(result, expected)
