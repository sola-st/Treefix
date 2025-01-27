# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_comment.py
parser = all_parsers
data = """# empty
random line
# second empty line
1,2,3
A,B,C
1,2.,4.
5.,NaN,10.0
"""
# This should ignore the first four lines (including comments).
expected = DataFrame(
    [[1.0, 2.0, 4.0], [5.0, np.nan, 10.0]], columns=["A", "B", "C"]
)
result = parser.read_csv(StringIO(data), comment="#", skiprows=4)
tm.assert_frame_equal(result, expected)
