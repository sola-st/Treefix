# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
# New match behavior introduced in 0.13
expected_dtype = "object" if any_string_dtype == "object" else "boolean"

values = Series(["fooBAD__barBAD", np.nan, "foo"], dtype=any_string_dtype)
result = values.str.match(".*(BAD[_]+).*(BAD)")
expected = Series([True, np.nan, False], dtype=expected_dtype)
tm.assert_series_equal(result, expected)

values = Series(
    ["fooBAD__barBAD", "BAD_BADleroybrown", np.nan, "foo"], dtype=any_string_dtype
)
result = values.str.match(".*BAD[_]+.*BAD")
expected = Series([True, True, np.nan, False], dtype=expected_dtype)
tm.assert_series_equal(result, expected)

result = values.str.match("BAD[_]+.*BAD")
expected = Series([False, True, np.nan, False], dtype=expected_dtype)
tm.assert_series_equal(result, expected)

values = Series(
    ["fooBAD__barBAD", "^BAD_BADleroybrown", np.nan, "foo"], dtype=any_string_dtype
)
result = values.str.match("^BAD[_]+.*BAD")
expected = Series([False, False, np.nan, False], dtype=expected_dtype)
tm.assert_series_equal(result, expected)

result = values.str.match("\\^BAD[_]+.*BAD")
expected = Series([False, True, np.nan, False], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
