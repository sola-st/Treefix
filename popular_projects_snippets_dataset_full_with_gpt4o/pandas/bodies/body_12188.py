# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_usecols_basic.py
# see gh-4201: test that index_col as integer reflects usecols
parser = all_parsers
data = "a,b,c,d\nA,a,1,one\nB,b,2,two"
expected = DataFrame({"c": [1, 2]}, index=Index(["a", "b"], name="b"))

result = parser.read_csv(StringIO(data), usecols=usecols, index_col=index_col)
tm.assert_frame_equal(result, expected)
