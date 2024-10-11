# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_python_parser_only.py
# see gh-17333
#
# csv.Sniffer in Python treats "o" as separator.
data = "aob\n1o2\n3o4"
parser = python_parser_only
expected = DataFrame({"a": [1, 3], "b": [2, 4]})

result = parser.read_csv(StringIO(data), sep=None)
tm.assert_frame_equal(result, expected)
