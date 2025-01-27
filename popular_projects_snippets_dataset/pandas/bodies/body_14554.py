# Extracted from ./data/repos/pandas/pandas/tests/io/test_clipboard.py
kwargs = build_kwargs(sep, excel)
df.to_clipboard(**kwargs)
result = read_clipboard(sep=r"\s+")
assert result.to_string() == df.to_string()
assert df.shape == result.shape
