# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_string.py
df = DataFrame([[0] * 11] * 4)
assert df.to_string(index=False, max_cols=max_cols, max_rows=max_rows) == expected
