# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
parser = all_parsers
data = """A,B,C
ignore,this,row
1,NA,3
-1.#IND,5,baz
7,8,NaN
"""
expected = DataFrame(
    [[1.0, np.nan, 3], [np.nan, 5, np.nan], [7, 8, np.nan]], columns=["A", "B", "C"]
)
result = parser.read_csv(StringIO(data), na_values=na_values, skiprows=[1])
tm.assert_frame_equal(result, expected)
