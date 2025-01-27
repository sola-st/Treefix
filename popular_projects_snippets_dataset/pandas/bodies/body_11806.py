# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# GH: 35958
f = StringIO("a  b  c\n1 -2 -3\n4  5   6")
parser = all_parsers
result = parser.read_table(f, delim_whitespace=True)
expected = DataFrame({"a": [1, 4], "b": [-2, 5], "c": [-3, 6]})
tm.assert_frame_equal(result, expected)
