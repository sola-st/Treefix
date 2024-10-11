# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_mangle_dupes.py
# see gh-17060
parser = all_parsers

result = parser.read_csv(StringIO(data))
tm.assert_frame_equal(result, expected)
