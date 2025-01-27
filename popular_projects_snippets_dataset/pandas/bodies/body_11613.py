# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_empty.py
# see gh-14712
parser = all_parsers
data = "a,b"

result = parser.read_csv(StringIO(data), header=0, dtype=dtype)
tm.assert_frame_equal(result, expected)
