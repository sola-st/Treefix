# Extracted from ./data/repos/pandas/pandas/tests/strings/test_case_justify.py
# test values are: two words less than width, two words equal to width,
# two words greater than width, one word less than width, one word
# equal to width, one word greater than width, multiple tokens with
# trailing whitespace equal to width
s = Series(
    [
        "hello world",
        "hello world!",
        "hello world!!",
        "abcdefabcde",
        "abcdefabcdef",
        "abcdefabcdefa",
        "ab ab ab ab ",
        "ab ab ab ab a",
        "\t",
    ],
    dtype=any_string_dtype,
)

# expected values
expected = Series(
    [
        "hello world",
        "hello world!",
        "hello\nworld!!",
        "abcdefabcde",
        "abcdefabcdef",
        "abcdefabcdef\na",
        "ab ab ab ab",
        "ab ab ab ab\na",
        "",
    ],
    dtype=any_string_dtype,
)

result = s.str.wrap(12, break_long_words=True)
tm.assert_series_equal(result, expected)
