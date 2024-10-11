# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_python_parser_only.py
# see gh-6893
data = "      A B C\na b c\n1 3 7 0 3 6\n3 1 4 1 5 9"
parser = python_parser_only

expected = DataFrame.from_records(
    [(1, 3, 7, 0, 3, 6), (3, 1, 4, 1, 5, 9)],
    columns=list("abcABC"),
    index=list("abc"),
)
result = parser.read_csv(StringIO(data), sep=r"\s+")
tm.assert_frame_equal(result, expected)
