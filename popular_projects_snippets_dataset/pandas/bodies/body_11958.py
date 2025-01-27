# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
data = """\
A,B
1,A
nan,B
3,C
"""
parser = all_parsers
result = parser.read_csv(StringIO(data), na_values=["B"], na_filter=na_filter)

expected = DataFrame(row_data, columns=["A", "B"])
tm.assert_frame_equal(result, expected)
