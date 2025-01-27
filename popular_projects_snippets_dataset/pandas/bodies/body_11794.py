# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
parser = all_parsers
data = """

\t  \t\t
\t
A,B,C
\t    1,2.,4.
5.,NaN,10.0
"""
expected = DataFrame([[1, 2.0, 4.0], [5.0, np.nan, 10.0]], columns=["A", "B", "C"])
result = parser.read_csv(StringIO(data))
tm.assert_frame_equal(result, expected)
