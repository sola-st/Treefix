# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
# GH 32806
ser = Series(
    ["fooBAD__barBAD", "BAD_BADleroybrown", np.nan, "foo"], dtype=any_string_dtype
)
result = ser.str.fullmatch(".*BAD[_]+.*BAD")
expected_dtype = "object" if any_string_dtype == "object" else "boolean"
expected = Series([True, False, np.nan, False], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
