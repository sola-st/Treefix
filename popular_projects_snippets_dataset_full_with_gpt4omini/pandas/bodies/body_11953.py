# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
data = """\
A,B,C
a,1,one
b,2,two
,3,three
d,4,nan
e,5,five
nan,6,
g,7,seven
"""
parser = all_parsers
result = parser.read_csv(StringIO(data), **kwargs)
tm.assert_frame_equal(result, expected)
