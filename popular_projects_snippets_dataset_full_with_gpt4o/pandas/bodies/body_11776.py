# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
data = """A,B,C
a,1,2
b,3,4
c,4,5
"""
parser = all_parsers
expected = DataFrame({"A": ["a", "b", "c"], "B": [1, 3, 4], "C": [2, 4, 5]})
result = parser.read_csv(StringIO(data))
tm.assert_frame_equal(result, expected)
