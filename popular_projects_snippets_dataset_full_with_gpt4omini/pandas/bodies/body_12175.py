# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_parse_dates.py
# see gh-9755
data = """a,b,c,d,e
0,1,2014-01-01,09:00,4
0,1,2014-01-02,10:00,4"""
parser = all_parsers
parse_dates = [[1, 2]]

cols = {
    "a": [0, 0],
    "c_d": [Timestamp("2014-01-01 09:00:00"), Timestamp("2014-01-02 10:00:00")],
}
expected = DataFrame(cols, columns=["c_d", "a"])
result = parser.read_csv(StringIO(data), usecols=usecols, parse_dates=parse_dates)
tm.assert_frame_equal(result, expected)
