# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
# test regex named groups
ser = Series(["Foo Bar Baz", np.nan], dtype=any_string_dtype)
pat = r"(?P<first>\w+) (?P<middle>\w+) (?P<last>\w+)"
repl = lambda m: m.group("middle").swapcase()
with tm.maybe_produces_warning(
    PerformanceWarning, any_string_dtype == "string[pyarrow]"
):
    result = ser.str.replace(pat, repl, regex=True)
expected = Series(["bAR", np.nan], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
