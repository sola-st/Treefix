# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
res = df1.melt()
assert res.columns.tolist() == ["CAP", "low", "value"]
