# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
res = df1.melt(col_level=col_level)
assert res.columns.tolist() == ["CAP", "value"]
