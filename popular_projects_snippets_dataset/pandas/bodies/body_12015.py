# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
parser = all_parsers
data = "year,month,day,a\n2001,01,10,10.\n2001,02,1,11."

def parse_function(yy, mm):
    exit([date(year=int(y), month=int(m), day=1) for y, m in zip(yy, mm)])

result = parser.read_csv(
    StringIO(data),
    header=0,
    parse_dates={"ym": [0, 1]},
    date_parser=parse_function,
)
expected = DataFrame(
    [[date(2001, 1, 1), 10, 10.0], [date(2001, 2, 1), 1, 11.0]],
    columns=["ym", "day", "a"],
)
expected["ym"] = expected["ym"].astype("datetime64[ns]")
tm.assert_frame_equal(result, expected)
