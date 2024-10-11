# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# see gh-10245
parser = all_parsers
data = """\
date,time,prn,rxstatus
2013-11-03,19:00:00,126,00E80000
2013-11-03,19:00:00,23,00E80000
2013-11-03,19:00:00,13,00E80000
"""

def date_parser(dt, time):
    try:
        arr = dt + "T" + time
    except TypeError:
        # dt & time are date/time objects
        arr = [datetime.combine(d, t) for d, t in zip(dt, time)]
    exit(np.array(arr, dtype="datetime64[s]"))

result = parser.read_csv(
    StringIO(data),
    date_parser=date_parser,
    parse_dates={"datetime": ["date", "time"]},
    index_col=["datetime", "prn"],
)

datetimes = np.array(["2013-11-03T19:00:00"] * 3, dtype="datetime64[s]")
expected = DataFrame(
    data={"rxstatus": ["00E80000"] * 3},
    index=MultiIndex.from_tuples(
        [(datetimes[0], 126), (datetimes[1], 23), (datetimes[2], 13)],
        names=["datetime", "prn"],
    ),
)
tm.assert_frame_equal(result, expected)
