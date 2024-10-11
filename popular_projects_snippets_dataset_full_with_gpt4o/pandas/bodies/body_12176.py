# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_parse_dates.py
# see gh-13604
parser = all_parsers
data = """2008-02-07 09:40,1032.43
2008-02-07 09:50,1042.54
2008-02-07 10:00,1051.65"""

names = ["date", "values"]
usecols = names[:]
parse_dates = [0]

index = Index(
    [
        Timestamp("2008-02-07 09:40"),
        Timestamp("2008-02-07 09:50"),
        Timestamp("2008-02-07 10:00"),
    ],
    name="date",
)
cols = {"values": [1032.43, 1042.54, 1051.65]}
expected = DataFrame(cols, index=index)

result = parser.read_csv(
    StringIO(data),
    parse_dates=parse_dates,
    index_col=0,
    usecols=usecols,
    header=None,
    names=names,
)
tm.assert_frame_equal(result, expected)
