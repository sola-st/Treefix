# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
result = melt(df)
assert result.columns.tolist() == ["variable", "value"]
