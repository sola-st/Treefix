# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# see gh-10476
data = """index,A,B,C,D
foo,2,3,4,5
bar,7,8,9,10
baz,12,13,14,15
qux,12,13,14,15
foo2,12,13,14,15
bar2,12,13,14,15
"""
expected = DataFrame(
    [["foo", 2, 3, 4, 5], ["bar", 7, 8, 9, 10], ["baz", 12, 13, 14, 15]],
    columns=["index", "A", "B", "C", "D"],
)
parser = all_parsers

result = parser.read_csv(StringIO(data), nrows=nrows)
tm.assert_frame_equal(result, expected)
