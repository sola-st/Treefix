# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_melt.py
result = df.melt()
assert result.columns.tolist() == ["variable", "value"]

result1 = df.melt(id_vars=["id1"])
assert result1.columns.tolist() == ["id1", "variable", "value"]

result2 = df.melt(id_vars=["id1", "id2"])
assert result2.columns.tolist() == ["id1", "id2", "variable", "value"]
