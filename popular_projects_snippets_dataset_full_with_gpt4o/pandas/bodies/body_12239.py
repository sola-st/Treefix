# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_quoting.py
# see gh-14477
data = "a\n1"
parser = all_parsers
expected = DataFrame({"a": [1]})

result = parser.read_csv(StringIO(data), quotechar=quotechar)
tm.assert_frame_equal(result, expected)
