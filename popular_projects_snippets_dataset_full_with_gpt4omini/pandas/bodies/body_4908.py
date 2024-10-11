# Extracted from ./data/repos/pandas/pandas/tests/strings/test_find_replace.py
obj = index_or_series(
    ["abcdefg", "abcc", "cdddfg", "cdefggg"], dtype=any_string_dtype
)
table = str.maketrans("abc", "cde")
result = obj.str.translate(table)
expected = index_or_series(
    ["cdedefg", "cdee", "edddfg", "edefggg"], dtype=any_string_dtype
)
tm.assert_equal(result, expected)
