# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_textreader.py
data = "123,456\n12,500"

reader = TextReader(StringIO(data), delimiter=":", thousands=",", header=None)
result = reader.read()

expected = np.array([123456, 12500], dtype=np.int64)
tm.assert_almost_equal(result[0], expected)
