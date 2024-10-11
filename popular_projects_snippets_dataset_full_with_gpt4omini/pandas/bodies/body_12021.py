# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
parser = all_parsers
expected = DataFrame({0: [date_string]}, dtype="object")
result = parser.read_csv_check_warnings(
    UserWarning,
    "Could not infer format",
    StringIO(date_string),
    header=None,
    parse_dates=[0],
)
tm.assert_frame_equal(result, expected)
