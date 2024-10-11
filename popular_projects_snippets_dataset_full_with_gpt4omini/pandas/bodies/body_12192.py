# Extracted from ./data/repos/pandas/pandas/tests/io/parser/usecols/test_usecols_basic.py
# GH#9098
parser = all_parsers
data = """a,b,c,d
1,2,3,4
"""
result = parser.read_csv(StringIO(data), usecols=["b", "c", "d"], index_col="d")
expected = DataFrame({"b": [2], "c": [3]}, index=Index([4], name="d"))
tm.assert_frame_equal(result, expected)
