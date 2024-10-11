# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
# see gh-19227
data = "a,b\n,2"
parser = all_parsers
result = parser.read_csv(
    StringIO(data), na_values={"b": ["2"]}, keep_default_na=False
)
expected = DataFrame({"a": [""], "b": [np.nan]})
tm.assert_frame_equal(result, expected)
