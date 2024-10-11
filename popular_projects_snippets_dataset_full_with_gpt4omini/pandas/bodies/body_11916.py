# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_index_col.py
# GH#38549
parser = all_parsers
data = """a,b,c,d
e,f,g,h
x,y,1,2
"""
result = parser.read_csv(
    StringIO(data),
    header=[0, 1],
    index_col=1,
)
cols = MultiIndex.from_tuples(
    [("a", "e"), ("c", "g"), ("d", "h")], names=["b", "f"]
)
expected = DataFrame([["x", 1, 2]], columns=cols, index=["y"])
tm.assert_frame_equal(result, expected)
