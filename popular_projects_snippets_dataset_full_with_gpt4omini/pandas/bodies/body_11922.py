# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_textreader.py
data = "a,   b\na,   b\na,   b\na,   b"

reader = TextReader(StringIO(data), skipinitialspace=True, header=None)
result = reader.read()

tm.assert_numpy_array_equal(
    result[0], np.array(["a", "a", "a", "a"], dtype=np.object_)
)
tm.assert_numpy_array_equal(
    result[1], np.array(["b", "b", "b", "b"], dtype=np.object_)
)
