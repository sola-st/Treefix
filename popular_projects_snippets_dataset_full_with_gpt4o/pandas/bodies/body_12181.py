# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_usecols_basic.py
data = """\
a,b,c
1,2,3
4,5,6
7,8,9
10,11,12"""
parser = all_parsers
result = parser.read_csv(StringIO(data), usecols=usecols)

expected = DataFrame([[2, 3], [5, 6], [8, 9], [11, 12]], columns=["b", "c"])
tm.assert_frame_equal(result, expected)
