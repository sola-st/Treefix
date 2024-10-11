# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_textreader.py
data = "123.456\n12.500"

reader = TextFileReader(
    StringIO(data), delimiter=":", thousands=".", header=None
)
result = reader.read()

expected = DataFrame([123456, 12500])
tm.assert_frame_equal(result, expected)
