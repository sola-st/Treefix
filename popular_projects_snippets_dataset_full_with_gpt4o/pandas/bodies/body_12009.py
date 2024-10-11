# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
data = """\
D,T,A,B
date, time,a,b
2001-01-05, 09:00:00, 0.0, 10.
2001-01-06, 00:00:00, 1.0, 11.
"""
parser = all_parsers
result = parser.read_csv(
    StringIO(data),
    header=[0, 1],
    parse_dates={"date_time": [0, 1]},
    date_parser=pd.to_datetime,
)

expected_data = [
    [datetime(2001, 1, 5, 9, 0, 0), 0.0, 10.0],
    [datetime(2001, 1, 6, 0, 0, 0), 1.0, 11.0],
]
expected = DataFrame(expected_data, columns=["date_time", ("A", "a"), ("B", "b")])
tm.assert_frame_equal(result, expected)
