# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_python_parser_only.py
# see gh-3404
expected = DataFrame({"a": [1], "b": [2]})
parser = python_parser_only

data = "1" + sep + "2"
encoded_data = data.encode(encoding)

result = parser.read_csv(
    BytesIO(encoded_data), sep=sep, names=["a", "b"], encoding=encoding
)
tm.assert_frame_equal(result, expected)
