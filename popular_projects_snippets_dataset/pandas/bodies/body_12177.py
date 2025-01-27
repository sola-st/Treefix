# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_parse_dates.py
# see gh-14792
parser = all_parsers
data = """a,b,c,d,e,f,g,h,i,j
2016/09/21,1,1,2,3,4,5,6,7,8"""

usecols = list("abcdefghij")
parse_dates = [0]

cols = {
    "a": Timestamp("2016-09-21"),
    "b": [1],
    "c": [1],
    "d": [2],
    "e": [3],
    "f": [4],
    "g": [5],
    "h": [6],
    "i": [7],
    "j": [8],
}
expected = DataFrame(cols, columns=usecols)

result = parser.read_csv(StringIO(data), usecols=usecols, parse_dates=parse_dates)
tm.assert_frame_equal(result, expected)
