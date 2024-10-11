# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
# Regression test for gh-4678
#
# Make sure thousands separator and
# date parsing do not conflict.
parser = all_parsers
data = "06-02-2013;13:00;1-000.215"
expected = DataFrame(
    [[datetime(2013, 6, 2, 13, 0, 0), 1000.215]], columns=["Date", 2]
)

df = parser.read_csv(
    StringIO(data),
    sep=";",
    thousands="-",
    parse_dates={"Date": [0, 1]},
    header=None,
)
tm.assert_frame_equal(df, expected)
