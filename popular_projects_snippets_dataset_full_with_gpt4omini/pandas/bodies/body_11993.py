# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
data = """date,time,B,C
090131,0010,1,2
090228,1020,3,4
090331,0830,5,6
"""
parser = all_parsers
result = parser.read_csv_check_warnings(
    UserWarning,
    "Could not infer format",
    StringIO(data),
    index_col=0,
    parse_dates=parse_dates,
)
index = DatetimeIndex(
    [
        datetime(2009, 1, 31, 0, 10, 0),
        datetime(2009, 2, 28, 10, 20, 0),
        datetime(2009, 3, 31, 8, 30, 0),
    ],
    dtype=object,
    name="date_time",
)
expected = DataFrame({"B": [1, 3, 5], "C": [2, 4, 6]}, index=index)
tm.assert_frame_equal(result, expected)
