# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_header.py
# GH#22144
parser = all_parsers
data = "x,1\ny,2,5\nz,3\n"
result = parser.read_csv(
    StringIO(data), names=["a", "b"], header=None, on_bad_lines="skip"
)
expected = DataFrame({"a": ["x", "z"], "b": [1, 3]})
tm.assert_frame_equal(result, expected)
