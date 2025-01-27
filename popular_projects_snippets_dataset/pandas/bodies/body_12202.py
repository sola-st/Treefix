# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_usecols_basic.py
data = "a,b,c,d\n1,2,3,4\n5,6,7,8"
names = ["A", "B", "C", "D"]
parser = all_parsers

result = parser.read_csv(StringIO(data), header=0, names=names, usecols=usecols)
expected = DataFrame({"A": [1, 5], "C": [3, 7]})
tm.assert_frame_equal(result, expected)
