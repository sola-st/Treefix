# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_inf.py
parser = all_parsers
data = """\
,A
a,Infinity
b,-Infinity
c,+Infinity
"""
expected = DataFrame(
    {"A": [float("infinity"), float("-infinity"), float("+infinity")]},
    index=["a", "b", "c"],
)
result = parser.read_csv(StringIO(data), index_col=0, na_filter=na_filter)
tm.assert_frame_equal(result, expected)
