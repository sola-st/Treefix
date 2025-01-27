# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_iterator.py
# gh-3967: stopping iteration when chunksize is specified
parser = all_parsers
data = """A,B,C
foo,1,2,3
bar,4,5,6
baz,7,8,9
"""

with parser.read_csv(StringIO(data), chunksize=1) as reader:
    result = list(reader)

assert len(result) == 3
expected = DataFrame(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    index=["foo", "bar", "baz"],
    columns=["A", "B", "C"],
)
tm.assert_frame_equal(concat(result), expected)
