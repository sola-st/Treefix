# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
parser = all_parsers
data = """A,B,C
a,b,c
d,,f
,g,h
"""
result = parser.read_csv(StringIO(data))
expected = DataFrame(
    [["a", "b", "c"], ["d", np.nan, "f"], [np.nan, "g", "h"]],
    columns=["A", "B", "C"],
)
tm.assert_frame_equal(result, expected)
