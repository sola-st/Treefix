# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
# see gh-3611: with an odd float format, we can't match
# the string "999.0" exactly but still need float matching
parser = all_parsers
expected = DataFrame([[np.nan, 1.2], [2.0, np.nan], [3.0, 4.5]], columns=["A", "B"])

result = parser.read_csv(StringIO(data), na_values=na_values)
tm.assert_frame_equal(result, expected)
