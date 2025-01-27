# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_index_col.py
# GH#38292
parser = all_parsers
result = parser.read_csv(StringIO("a0,a1,a2\n"), header=[0], index_col=0)
expected = DataFrame(
    [],
    columns=["a1", "a2"],
    index=Index([], name="a0"),
)
tm.assert_frame_equal(result, expected)
