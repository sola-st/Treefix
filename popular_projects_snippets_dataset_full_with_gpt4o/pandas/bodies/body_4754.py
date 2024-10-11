# Extracted from ./data/repos/pandas/pandas/tests/strings/test_strings.py

obj = index_or_series(
    ["ABCDEFG", "BCDEFEF", "DEFGHIJEF", "EFGHEF"], dtype=any_string_dtype
)
expected_dtype = np.int64 if any_string_dtype == "object" else "Int64"
expected = index_or_series(expected, dtype=expected_dtype)

result = getattr(obj.str, method)(sub, start, end)

if index_or_series is Series:
    tm.assert_series_equal(result, expected)
else:
    tm.assert_index_equal(result, expected)

# compare with standard library
expected = [getattr(item, method)(sub, start, end) for item in obj]
assert list(result) == expected
