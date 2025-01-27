# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# see gh-2442
data = """A,B,C
1,2,3,
4,5,6,
7,8,9,"""
parser = all_parsers
result = parser.read_csv(StringIO(data), index_col=False)

expected = DataFrame({"A": [1, 4, 7], "B": [2, 5, 8], "C": [3, 6, 9]})
tm.assert_frame_equal(result, expected)
