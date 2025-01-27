# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
data = """\
a,b,c,d
0,NA,1,5
"""
parser = all_parsers
result = parser.read_csv(StringIO(data), na_values=set(), index_col=index_col)
tm.assert_frame_equal(result, expected)
