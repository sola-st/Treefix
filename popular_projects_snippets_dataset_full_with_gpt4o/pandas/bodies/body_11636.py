# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_dtypes_basic.py
data = "0\n1"
parser = all_parsers
expected = DataFrame([0, 1], dtype=dtype)

result = parser.read_csv(StringIO(data), header=None, dtype=dtype)
tm.assert_frame_equal(expected, result)
