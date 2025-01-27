# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby.py
# see gh-1291
result = df.groupby(df["A"].values).sum()
assert result.index.name is None

result = df.groupby([df["A"].values, df["B"].values]).sum()
assert result.index.names == (None, None)
