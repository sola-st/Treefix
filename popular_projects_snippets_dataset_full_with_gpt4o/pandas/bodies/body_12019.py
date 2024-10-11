# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# see gh-2697
#
# Date parsing should fail, so we leave the data untouched
# (i.e. float precision should remain unchanged).
parser = all_parsers

result = parser.read_csv(StringIO(data), parse_dates=parse_dates)
tm.assert_frame_equal(result, expected)
