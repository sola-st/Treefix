# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
# GH 15446
ser = Series(["fooBAD__barBAD", np.nan], dtype=any_string_dtype)

# test with compiled regex
pat = re.compile(r"BAD_*")
with tm.maybe_produces_warning(
    PerformanceWarning, any_string_dtype == "string[pyarrow]"
):
    result = ser.str.replace(pat, "", regex=True)
expected = Series(["foobar", np.nan], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)

with tm.maybe_produces_warning(
    PerformanceWarning, any_string_dtype == "string[pyarrow]"
):
    result = ser.str.replace(pat, "", n=1, regex=True)
expected = Series(["foobarBAD", np.nan], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
