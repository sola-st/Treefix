# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_file_buffer_url.py
# see gh-5500
parser = all_parsers
data = "a,b\n1\x1a,2"

expected = DataFrame([["1\x1a", 2]], columns=["a", "b"])
result = parser.read_csv(StringIO(data))
tm.assert_frame_equal(result, expected)
