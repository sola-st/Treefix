# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series(["foo", "foofoo", np.nan, "foooofooofommmfoo"], dtype=any_string_dtype)
result = ser.str.count("f[o]+")
expected_dtype = np.float64 if any_string_dtype == "object" else "Int64"
expected = Series([1, 2, np.nan, 4], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
