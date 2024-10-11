# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
# see gh-19227
#
# Scalar values shouldn't cause the parsing to crash or fail.
data = "a,b\n1,2"
parser = all_parsers
df = parser.read_csv(StringIO(data), na_values={"b": 2}, keep_default_na=False)
expected = DataFrame({"a": [1], "b": [np.nan]})
tm.assert_frame_equal(df, expected)
