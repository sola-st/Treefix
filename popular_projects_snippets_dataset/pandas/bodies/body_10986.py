# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
result = df.groupby(["A", "B"])["C"].apply(len)
assert result.index.names[:2] == ("A", "B")
