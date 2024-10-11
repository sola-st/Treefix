# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
# see gh-15835
data = "a,1\nb,2"
parser = all_parsers
expected = DataFrame({"1": [2]}, index=Index(["b"], name="a"))

result = parser.read_csv(StringIO(data), index_col=0, keep_default_na=False)
tm.assert_frame_equal(result, expected)
