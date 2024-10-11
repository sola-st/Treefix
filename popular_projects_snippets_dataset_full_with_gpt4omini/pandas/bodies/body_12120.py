# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_encoding.py
# GH16218 Verify parsing of data with encoded special characters
# Data contains a Unicode 'FULLWIDTH COLON' (U+FF1A) at position (0,"a")
data = "a\tb\n：foo\t0\nbar\t1\nbaz\t2"
encoded_data = BytesIO(data.encode(encoding))
result = read_csv(encoded_data, delimiter="\t", encoding=encoding)

expected = DataFrame(data=[["：foo", 0], ["bar", 1], ["baz", 2]], columns=["a", "b"])
tm.assert_frame_equal(result, expected)
