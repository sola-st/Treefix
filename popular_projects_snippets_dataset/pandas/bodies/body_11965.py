# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
# see gh-5239
#
# Don't parse NA-values in index unless na_filter=True
parser = all_parsers
data = "a,b,c\n1,,3\n4,5,6"

expected = DataFrame({"a": [1, 4], "c": [3, 6]}, index=Index(index_data, name="b"))
result = parser.read_csv(StringIO(data), index_col=[1], na_filter=na_filter)
tm.assert_frame_equal(result, expected)
