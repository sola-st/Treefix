# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# see gh-3374, gh-6607
parser = all_parsers
data = " a b c\n 1 2 3\n 4 5 6\n 7 8 9"
result = parser.read_csv(StringIO(data), sep=r"\s+")

expected = DataFrame({"a": [1, 4, 7], "b": [2, 5, 8], "c": [3, 6, 9]})
tm.assert_frame_equal(result, expected)
