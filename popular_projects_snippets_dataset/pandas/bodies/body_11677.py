# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_header.py
# see gh-18062
parser = all_parsers

result = parser.read_csv(StringIO(data), header=[0, 1])
tm.assert_frame_equal(result, expected)
