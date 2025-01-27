# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_usecols_basic.py
# GH#46997
parser = all_parsers
usecols = lambda header: header.strip() in ["a", "b", "c"]
result = parser.read_csv(StringIO("a,b\nx,y,z"), index_col=False, usecols=usecols)
expected = DataFrame({"a": ["x"], "b": "y"})
tm.assert_frame_equal(result, expected)
