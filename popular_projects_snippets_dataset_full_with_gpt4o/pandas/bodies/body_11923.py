# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_textreader.py
data = "True\nFalse\nTrue\nTrue"

reader = TextReader(StringIO(data), header=None)
result = reader.read()

assert result[0].dtype == np.bool_
