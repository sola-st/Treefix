# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_get_set.py
# motivating example from #3742
lev1 = ["hans", "hans", "hans", "grethe", "grethe", "grethe"]
lev2 = ["1", "2", "3"] * 2
idx = MultiIndex.from_arrays([lev1, lev2], names=["Name", "Number"])
df = pd.DataFrame(
    np.random.randn(6, 4), columns=["one", "two", "three", "four"], index=idx
)
df = df.sort_index()
assert df._is_copy is None
assert df.index.names == ("Name", "Number")
df.at[("grethe", "4"), "one"] = 99.34
assert df._is_copy is None
assert df.index.names == ("Name", "Number")
