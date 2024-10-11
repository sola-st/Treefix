# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series(
    ["foo", "fooo", "fooooo", np.nan, "fooooooo", "foo\n", "あ"],
    dtype=any_string_dtype,
)
result = ser.str.len()
expected_dtype = "float64" if any_string_dtype == "object" else "Int64"
expected = Series([3, 4, 6, np.nan, 8, 4, 1], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
