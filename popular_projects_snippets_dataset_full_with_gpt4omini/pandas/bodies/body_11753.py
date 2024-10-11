# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_index.py
data = "x,y,z"
parser = all_parsers
result = parser.read_csv(StringIO(data), index_col=[1, 0])

expected = DataFrame(
    columns=["z"], index=MultiIndex.from_arrays([[]] * 2, names=["y", "x"])
)
tm.assert_frame_equal(result, expected)
