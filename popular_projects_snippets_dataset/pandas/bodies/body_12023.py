# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
parser = all_parsers
expected = DataFrame({0: [expected]}, dtype="datetime64[ns]")
warning_msg = (
    "Parsing dates in .* format when dayfirst=.* was specified. "
    "Pass `dayfirst=.*` or specify a format to silence this warning."
)
result = parser.read_csv_check_warnings(
    UserWarning,
    warning_msg,
    StringIO(date_string),
    header=None,
    dayfirst=dayfirst,
    parse_dates=[0],
)
tm.assert_frame_equal(result, expected)
