# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
parser = all_parsers
data = """A,B
foo,bar
NA,baz
NaN,nan
"""
expected = DataFrame(
    [["foo", "bar"], [np.nan, "baz"], [np.nan, np.nan]], columns=["A", "B"]
)
result = parser.read_csv(StringIO(data))
tm.assert_frame_equal(result, expected)
