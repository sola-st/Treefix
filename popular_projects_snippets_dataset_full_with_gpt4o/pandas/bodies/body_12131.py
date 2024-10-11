# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_python_parser_only.py
# see gh-6607: sniff separator
parser = python_parser_only
result = parser.read_csv(StringIO("1,2"), names=["a", "b"], header=None, sep=None)

expected = DataFrame({"a": [1], "b": [2]})
tm.assert_frame_equal(result, expected)
