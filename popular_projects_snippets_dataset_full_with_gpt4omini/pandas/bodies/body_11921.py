# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_textreader.py
# should this be optional?
data = "a\nb\na\nb\na"
reader = TextReader(StringIO(data), header=None)
result = reader.read()
assert len(set(map(id, result[0]))) == 2
