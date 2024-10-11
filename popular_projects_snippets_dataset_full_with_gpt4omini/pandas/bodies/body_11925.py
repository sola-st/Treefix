# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_textreader.py
data = 'a\n"hello\nthere"\nthis'

reader = TextReader(StringIO(data), header=None)
result = reader.read()

expected = np.array(["a", "hello\nthere", "this"], dtype=np.object_)
tm.assert_numpy_array_equal(result[0], expected)
