# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_ints.py
data = """A,B
1.0,1
2.0,2
3.0,3
"""
parser = all_parsers
result = parser.read_csv(StringIO(data))

expected = DataFrame([[1.0, 1], [2.0, 2], [3.0, 3]], columns=["A", "B"])
tm.assert_frame_equal(result, expected)
