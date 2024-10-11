# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_header.py
parser = all_parsers
data = """foo,1,2,3
bar,4,5,6
baz,7,8,9
"""
names = ["A", "B", "C"]
result = parser.read_csv(StringIO(data), names=names)

expected = DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    index=["foo", "bar", "baz"],
    columns=["A", "B", "C"],
)
tm.assert_frame_equal(result, expected)
