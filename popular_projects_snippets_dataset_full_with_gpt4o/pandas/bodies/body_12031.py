# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# GH#39365
data = """A,B,C
    1,3,20-09-01-01
    2,4,20-09-01-01
    """

parser = all_parsers
result = parser.read_csv_check_warnings(
    UserWarning,
    "Could not infer format",
    StringIO(data),
    parse_dates=[1],
    usecols=[1, 2],
    thousands="-",
)
expected = DataFrame({"B": [3, 4], "C": [Timestamp("20-09-2001 01:00:00")] * 2})
tm.assert_frame_equal(result, expected)
