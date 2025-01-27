# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
df = tm.makeDataFrame()
df.index.name = "name"

assert df.set_index(df.index).index.names == ["name"]

mi = MultiIndex.from_arrays(df[["A", "B"]].T.values, names=["A", "B"])
mi2 = MultiIndex.from_arrays(
    df[["A", "B", "A", "B"]].T.values, names=["A", "B", "C", "D"]
)

df = df.set_index(["A", "B"])

assert df.set_index(df.index).index.names == ["A", "B"]

# Check that set_index isn't converting a MultiIndex into an Index
assert isinstance(df.set_index(df.index).index, MultiIndex)

# Check actual equality
tm.assert_index_equal(df.set_index(df.index).index, mi)

idx2 = df.index.rename(["C", "D"])

# Check that [MultiIndex, MultiIndex] yields a MultiIndex rather
# than a pair of tuples
assert isinstance(df.set_index([df.index, idx2]).index, MultiIndex)

# Check equality
tm.assert_index_equal(df.set_index([df.index, idx2]).index, mi2)
