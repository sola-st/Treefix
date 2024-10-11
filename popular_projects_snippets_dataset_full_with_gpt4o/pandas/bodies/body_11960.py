# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
# see gh-12224
parser = all_parsers
names = ["a", "b"]
data = "1,2\n2,1"

result = parser.read_csv(StringIO(data), names=names, na_values=na_values)
expected = DataFrame(row_data, columns=names)
tm.assert_frame_equal(result, expected)
