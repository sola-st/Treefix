# Extracted from ./data/repos/pandas/pandas/tests/test_multilevel.py
index = MultiIndex.from_tuples(
    [("foo", "one"), ("foo", "two"), ("bar", "one"), ("bar", "two")]
)
df = DataFrame(np.random.randn(4, 4), index=index, columns=index)
df["Totals", ""] = df.sum(1)
df = df._consolidate()
