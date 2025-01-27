# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_index_col.py
# see gh-10413
data = "x,y"
parser = all_parsers
result = parser.read_csv(StringIO(data), index_col=False)

expected = DataFrame(columns=["x", "y"])
tm.assert_frame_equal(result, expected)
