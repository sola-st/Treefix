# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_parse_dates.py
# see gh-9755
s = """0,1,2014-01-01,09:00,4
0,1,2014-01-02,10:00,4"""
parse_dates = [[1, 2]]
parser = all_parsers

cols = {
    "a": [0, 0],
    "c_d": [Timestamp("2014-01-01 09:00:00"), Timestamp("2014-01-02 10:00:00")],
}
expected = DataFrame(cols, columns=["c_d", "a"])

result = parser.read_csv(
    StringIO(s), names=names, parse_dates=parse_dates, usecols=usecols
)
tm.assert_frame_equal(result, expected)
