# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_skiprows.py
# GH#44021
data = """a,b
1,a
2,b
3,c
4,d
5,e
6,f
7,g
8,h
"""
parser = all_parsers
result = parser.read_csv(StringIO(data), nrows=5, skiprows=[2, 4, 6])
expected = DataFrame({"a": [1, 3, 5, 7, 8], "b": ["a", "c", "e", "g", "h"]})
tm.assert_frame_equal(result, expected)
