# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# GH#33699
parser = all_parsers
data = StringIO("""x,y\n1,2""")
result = parser.read_csv_check_warnings(
    UserWarning,
    "Could not infer format",
    data,
    parse_dates=["B"],
    names=["B"],
)
expected = DataFrame({"B": ["y", "2"]}, index=["x", "1"])
tm.assert_frame_equal(result, expected)
