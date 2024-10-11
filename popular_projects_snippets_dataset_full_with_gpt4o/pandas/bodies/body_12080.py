# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_comment.py
parser = all_parsers
data = """# empty
# second empty line
# third empty line
X,Y,Z
1,2,3
A,B,C
1,2.,4.
5.,NaN,10.0
"""
# Skiprows should skip the first 4 lines (including comments),
# while header should start from the second non-commented line,
# starting with line 5.
expected = DataFrame(
    [[1.0, 2.0, 4.0], [5.0, np.nan, 10.0]], columns=["A", "B", "C"]
)
result = parser.read_csv(StringIO(data), comment="#", skiprows=4, header=1)
tm.assert_frame_equal(result, expected)
