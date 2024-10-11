# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_encoding.py
encoding = "cp1255"
parser = all_parsers

data = BytesIO("שלום:1234\n562:123".encode(encoding))
result = parser.read_csv(data, sep=":", encoding=encoding)

expected = DataFrame([[562, 123]], columns=["שלום", "1234"])
tm.assert_frame_equal(result, expected)
