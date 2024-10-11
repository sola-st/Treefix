# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_header.py
# See gh-7773
parser = all_parsers
expected = DataFrame(columns=["a", "b", "c"])

result = parser.read_csv(StringIO("a,b,c"), **kwargs)
tm.assert_frame_equal(result, expected)
