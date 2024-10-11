# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
parser = all_parsers
data = """\
year,month,day,hour,minute,second,a,b
2001,01,05,10,00,0,0.0,10.
2001,01,5,10,0,00,1.,11.
"""
result = parser.read_csv(
    StringIO(data),
    header=0,
    date_parser=lambda x: pd.to_datetime(x, format="%Y %m %d %H %M %S"),
    parse_dates={"ymdHMS": [0, 1, 2, 3, 4, 5]},
)
expected = DataFrame(
    [
        [datetime(2001, 1, 5, 10, 0, 0), 0.0, 10.0],
        [datetime(2001, 1, 5, 10, 0, 0), 1.0, 11.0],
    ],
    columns=["ymdHMS", "a", "b"],
)
tm.assert_frame_equal(result, expected)
