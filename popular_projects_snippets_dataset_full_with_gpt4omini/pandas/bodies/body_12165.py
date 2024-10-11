# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_skiprows.py
# see gh-14459
parser = all_parsers
data = 'a"\nb"\na\n1'
expected = DataFrame({"a": [1]})

result = parser.read_csv(StringIO(data), skiprows=2)
tm.assert_frame_equal(result, expected)
