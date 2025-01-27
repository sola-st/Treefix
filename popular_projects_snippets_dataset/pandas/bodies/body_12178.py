# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_parse_dates.py
data = "a,b,c,d,e,f,g,h,i,j\n2016/09/21,1,1,2,3,4,5,6,7,8"
usecols = list("abcdefghij")
parse_dates = [[0, 1]]
parser = all_parsers

cols = {
    "a_b": "2016/09/21 1",
    "c": [1],
    "d": [2],
    "e": [3],
    "f": [4],
    "g": [5],
    "h": [6],
    "i": [7],
    "j": [8],
}
expected = DataFrame(cols, columns=["a_b"] + list("cdefghij"))

result = parser.read_csv_check_warnings(
    UserWarning,
    "Could not infer format",
    StringIO(data),
    usecols=usecols,
    parse_dates=parse_dates,
)
tm.assert_frame_equal(result, expected)
