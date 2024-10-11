# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_header.py
# see gh-2539
parser = all_parsers
expected = parser.read_csv(StringIO("1,2,3\n4,5,6"), names=["a", "b", "c"])

result = parser.read_csv(StringIO(data), names=["a", "b", "c"], header=header)
tm.assert_frame_equal(result, expected)
