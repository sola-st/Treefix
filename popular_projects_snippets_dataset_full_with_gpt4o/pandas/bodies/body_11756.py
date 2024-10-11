# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_chunksize.py
parser = all_parsers
data = """index,A,B,C,D
foo,2,3,4,5
bar,7,8,9,10
baz,12,13,14,15
qux,12,13,14,15
foo2,12,13,14,15
bar2,12,13,14,15
"""

expected = DataFrame(
    [
        ["foo", 2, 3, 4, 5],
        ["bar", 7, 8, 9, 10],
        ["baz", 12, 13, 14, 15],
        ["qux", 12, 13, 14, 15],
        ["foo2", 12, 13, 14, 15],
        ["bar2", 12, 13, 14, 15],
    ],
    columns=["index", "A", "B", "C", "D"],
)
expected = expected.set_index("index")

with parser.read_csv(StringIO(data), index_col=0, chunksize=2) as reader:
    chunks = list(reader)
tm.assert_frame_equal(chunks[0], expected[:2])
tm.assert_frame_equal(chunks[1], expected[2:4])
tm.assert_frame_equal(chunks[2], expected[4:])
