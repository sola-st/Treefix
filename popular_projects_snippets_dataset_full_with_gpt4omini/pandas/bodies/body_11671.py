# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_header.py
# GH 40442
parser = all_parsers
data = [[None, None], [1, 2], [3, 4]]
columns = MultiIndex.from_tuples([("a", "A"), ("b", "B")])
expected = DataFrame(data, columns=columns)
data = "a,b\nA,B\n,\n1,2\n3,4"
result = parser.read_csv(StringIO(data), header=[0, 1])
tm.assert_frame_equal(expected, result)
