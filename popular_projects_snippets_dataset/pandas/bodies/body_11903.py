# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_index_col.py
data = "x,y,z"
parser = all_parsers
result = parser.read_csv(StringIO(data), index_col=index_col)

expected = DataFrame(**kwargs)
tm.assert_frame_equal(result, expected)
