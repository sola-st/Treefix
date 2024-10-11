# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_encoding.py
parser = all_parsers
data = BytesIO("\u0141aski, Jan;1".encode())

result = parser.read_csv(data, sep=";", encoding="utf-8", header=None)
expected = DataFrame([["\u0141aski, Jan", 1]])
tm.assert_frame_equal(result, expected)
