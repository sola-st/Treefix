# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_usecols_basic.py
data = """\
a,b,c
1,2,3
4,5,6
7,8,9
10,11,12"""
parser = all_parsers
names = ["foo", "bar"]
result = parser.read_csv(StringIO(data), names=names, usecols=[1, 2], header=0)

expected = DataFrame([[2, 3], [5, 6], [8, 9], [11, 12]], columns=names)
tm.assert_frame_equal(result, expected)
