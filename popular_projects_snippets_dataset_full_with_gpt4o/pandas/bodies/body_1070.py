# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_setitem.py
# GH#7190
cols = ["A", "w", "l", "a", "x", "X", "d", "profit"]
index = MultiIndex.from_product(
    [np.arange(0, 100), np.arange(0, 80)], names=["time", "firm"]
)
t, n = 0, 2

df = DataFrame(
    np.nan,
    columns=cols,
    index=index,
)
self.check(target=df, indexers=((t, n), "X"), value=0)

df = DataFrame(-999, columns=cols, index=index)
self.check(target=df, indexers=((t, n), "X"), value=1)

df = DataFrame(columns=cols, index=index)
self.check(target=df, indexers=((t, n), "X"), value=2)

# gh-7218: assigning with 0-dim arrays
df = DataFrame(-999, columns=cols, index=index)
self.check(
    target=df,
    indexers=((t, n), "X"),
    value=np.array(3),
    expected=3,
)
