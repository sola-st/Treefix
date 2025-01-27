# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
parser = all_parsers
expected = DataFrame({0: [expected]}, dtype="datetime64[ns]")
result = parser.read_csv(
    StringIO(date_string), header=None, dayfirst=dayfirst, parse_dates=[0]
)
tm.assert_frame_equal(result, expected)
