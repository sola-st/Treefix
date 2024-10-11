# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
grouped = df.loc[:, ["C"]].groupby(df["A"])
result = grouped.agg(lambda x: x.mean())
assert result.index.name == "A"
