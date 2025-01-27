# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_c_parser_only.py
# see gh-23779
parser = c_parser_only
expected = DataFrame([[1, 2, 3], [4, 5, 6]])

with tm.ensure_clean() as path:
    with open(path, "w") as f:
        f.write("1,2,3\n4,5,6")

    with open(path, "rb") as f:
        result = parser.read_csv(f, header=None)
        tm.assert_frame_equal(result, expected)
