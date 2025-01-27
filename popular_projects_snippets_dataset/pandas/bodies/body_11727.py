# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_data_list.py
parser = all_parsers
data = """foo
bar baz
qux foo
foo
bar"""

result = parser.read_csv(StringIO(data), header=None)
expected = DataFrame(["foo", "bar baz", "qux foo", "foo", "bar"])
tm.assert_frame_equal(result, expected)
