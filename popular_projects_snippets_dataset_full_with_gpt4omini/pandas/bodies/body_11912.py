# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_index_col.py
# GH#38292
parser = all_parsers
result = parser.read_csv(StringIO("a0,a1,a2\nb0,b1,b2\n"), header=[0, 1])
expected = DataFrame(
    [], columns=MultiIndex.from_arrays([["a0", "a1", "a2"], ["b0", "b1", "b2"]])
)
tm.assert_frame_equal(result, expected)
