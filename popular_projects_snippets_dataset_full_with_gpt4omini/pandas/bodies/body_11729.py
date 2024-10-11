# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_iterator.py
parser = all_parsers
data = """A,B,C
foo,1,2,3
bar,4,5,6
baz,7,8,9
"""

with parser.read_csv(StringIO(data), iterator=True) as reader:
    result = list(reader)

expected = DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    index=["foo", "bar", "baz"],
    columns=["A", "B", "C"],
)
tm.assert_frame_equal(result[0], expected)
