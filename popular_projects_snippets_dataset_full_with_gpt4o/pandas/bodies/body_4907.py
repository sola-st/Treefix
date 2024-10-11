# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
ser = Series(
    ["ABCDEFG", np.nan, "DEFGHIJEF", np.nan, "XXXX"], dtype=any_string_dtype
)
expected_dtype = np.float64 if any_string_dtype == "object" else "Int64"

result = ser.str.find("EF")
expected = Series([4, np.nan, 1, np.nan, -1], dtype=expected_dtype)
tm.assert_series_equal(result, expected)

result = ser.str.rfind("EF")
expected = Series([4, np.nan, 7, np.nan, -1], dtype=expected_dtype)
tm.assert_series_equal(result, expected)

result = ser.str.find("EF", 3)
expected = Series([4, np.nan, 7, np.nan, -1], dtype=expected_dtype)
tm.assert_series_equal(result, expected)

result = ser.str.rfind("EF", 3)
expected = Series([4, np.nan, 7, np.nan, -1], dtype=expected_dtype)
tm.assert_series_equal(result, expected)

result = ser.str.find("EF", 3, 6)
expected = Series([4, np.nan, -1, np.nan, -1], dtype=expected_dtype)
tm.assert_series_equal(result, expected)

result = ser.str.rfind("EF", 3, 6)
expected = Series([4, np.nan, -1, np.nan, -1], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
