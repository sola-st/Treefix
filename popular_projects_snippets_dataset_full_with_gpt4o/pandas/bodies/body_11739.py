# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_ints.py
# These numbers fall right inside the int64-uint64
# range, so they should be parsed as string.
parser = all_parsers
result = parser.read_csv(StringIO(str(val)), header=None)

expected = DataFrame([val])
tm.assert_frame_equal(result, expected)
