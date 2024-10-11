# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_chunksize.py
# see gh-10022
parser = all_parsers
data = "\n hello\nworld\n"

result = parser.read_csv(StringIO(data), header=None)
expected = DataFrame([" hello", "world"])
tm.assert_frame_equal(result, expected)
