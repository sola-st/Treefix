# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_encoding.py
# see gh-13549
expected = DataFrame({"mb_num": [4.8], "multibyte": ["test"]})
parser = all_parsers

encoding = encoding_fmt.format(utf_value)
data = "mb_num,multibyte\n4.8,test".encode(encoding)

result = parser.read_csv(BytesIO(data), encoding=encoding)
tm.assert_frame_equal(result, expected)
