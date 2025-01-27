# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_textreader.py
data = '\\"hello world"\n\\"hello world"\n\\"hello world"'

reader = TextReader(StringIO(data), delimiter=",", header=None, escapechar="\\")
result = reader.read()
expected = {0: np.array(['"hello world"'] * 3, dtype=object)}
assert_array_dicts_equal(result, expected)
