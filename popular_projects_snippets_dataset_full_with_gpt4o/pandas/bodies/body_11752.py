# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_index.py
# see gh-10467
data = "x,y,z"
parser = all_parsers
result = parser.read_csv(StringIO(data), index_col=["x", "y"])

expected = DataFrame(
    columns=["z"], index=MultiIndex.from_arrays([[]] * 2, names=["x", "y"])
)
tm.assert_frame_equal(result, expected)
