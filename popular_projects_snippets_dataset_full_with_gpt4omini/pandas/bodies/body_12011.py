# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
parser = all_parsers
data = "year,month,day,a\n2001,01,10,10.\n2001,02,1,11."
result = parser.read_csv(
    StringIO(data),
    header=0,
    parse_dates={"ymd": [0, 1, 2]},
    date_parser=pd.to_datetime,
)

expected = DataFrame(
    [[datetime(2001, 1, 10), 10.0], [datetime(2001, 2, 1), 11.0]],
    columns=["ymd", "a"],
)
tm.assert_frame_equal(result, expected)
