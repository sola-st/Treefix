# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# see gh-6607
parser = all_parsers
result = parser.read_csv(StringIO(data), sep=r"\s+")
tm.assert_frame_equal(result, expected)
