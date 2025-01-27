# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py
ser = Series(
    ["A", "b", "Xy", "4", "3A", "", "TT", "55", "-", "  "], dtype=any_string_dtype
)
expected_dtype = "bool" if any_string_dtype == "object" else "boolean"
expected = Series(expected, dtype=expected_dtype)
result = getattr(ser.str, method)()
tm.assert_series_equal(result, expected)

# compare with standard library
expected = [getattr(item, method)() for item in ser]
assert list(result) == expected
