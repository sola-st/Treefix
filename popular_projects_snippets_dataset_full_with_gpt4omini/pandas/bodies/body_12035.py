# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# GH#11019
parser = all_parsers
data = "a,b,c\n1970-01-01,2,3,4"
result = parser.read_csv_check_warnings(
    UserWarning,
    "Could not infer format",
    StringIO(data),
    parse_dates=["a"],
)
expected = DataFrame({"a": "2", "b": 3, "c": 4}, index=["1970-01-01"])
tm.assert_frame_equal(result, expected)
