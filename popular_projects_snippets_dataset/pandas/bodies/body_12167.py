# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_skiprows.py
parser = all_parsers
data = "0,a\n1,b\n2,c\n3,d\n4,e"
expected = DataFrame([[1, "b"], [3, "d"]])

result = parser.read_csv(
    StringIO(data), header=None, skiprows=lambda x: x not in [1, 3]
)
tm.assert_frame_equal(result, expected)
