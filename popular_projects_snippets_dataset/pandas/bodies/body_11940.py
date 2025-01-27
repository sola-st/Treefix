# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_textreader.py
nice_text = text.replace("\r", "\r\n")
result = TextReader(StringIO(text), **kwargs).read()
expected = TextReader(StringIO(nice_text), **kwargs).read()
assert_array_dicts_equal(result, expected)
