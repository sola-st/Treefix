# Extracted from ./data/repos/pandas/pandas/tests/io/test_clipboard.py
df.to_clipboard(excel=False, sep=None)
result = read_clipboard()
assert df.to_string() == result.to_string()
assert df.shape == result.shape
