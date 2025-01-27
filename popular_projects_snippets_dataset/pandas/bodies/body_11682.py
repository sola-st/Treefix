# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_header.py
# GH#22144
parser = all_parsers
data = "x,1,5\ny,2\nz,3\n"
result = parser.read_csv(StringIO(data), names=["a", "b"], header=None)
expected = DataFrame(
    {"a": [1, 2, 3], "b": [5, np.nan, np.nan]}, index=["x", "y", "z"]
)
tm.assert_frame_equal(result, expected)
