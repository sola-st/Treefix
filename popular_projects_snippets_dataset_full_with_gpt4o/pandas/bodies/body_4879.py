# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
ser = Series([b"abcd,\xc3\xa0".decode("utf-8")], dtype=any_string_dtype)
expected = Series([b"abcd, \xc3\xa0".decode("utf-8")], dtype=any_string_dtype)
with tm.maybe_produces_warning(
    PerformanceWarning, any_string_dtype == "string[pyarrow]"
):
    result = ser.str.replace(r"(?<=\w),(?=\w)", ", ", flags=re.UNICODE, regex=True)
tm.assert_series_equal(result, expected)
