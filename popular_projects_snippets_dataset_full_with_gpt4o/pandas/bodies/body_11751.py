# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_index.py
# see gh-10184
data = "x,y"
parser = all_parsers
result = parser.read_csv(StringIO(data), index_col=0)

expected = DataFrame(columns=["y"], index=Index([], name="x"))
tm.assert_frame_equal(result, expected)
