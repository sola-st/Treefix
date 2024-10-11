# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
parser = all_parsers
data = """A,B,C,D
1,2,3,4
1,3,3,
1,4,5"""

result = parser.read_csv(StringIO(data))
expected = DataFrame(
    [[1, 2, 3, 4], [1, 3, 3, np.nan], [1, 4, 5, np.nan]],
    columns=["A", "B", "C", "D"],
)
tm.assert_frame_equal(result, expected)
