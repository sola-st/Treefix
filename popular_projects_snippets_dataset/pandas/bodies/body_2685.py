# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename_axis.py
# GH#19978
mi = MultiIndex.from_product([["a", "b", "c"], [1, 2]], names=["ll", "nn"])
df = DataFrame(
    {"x": list(range(len(mi))), "y": [i * 10 for i in range(len(mi))]}, index=mi
)

# Test for rename of the Index object of columns
result = df.rename_axis("cols", axis=1)
tm.assert_index_equal(result.columns, Index(["x", "y"], name="cols"))

# Test for rename of the Index object of columns using dict
result = result.rename_axis(columns={"cols": "new"}, axis=1)
tm.assert_index_equal(result.columns, Index(["x", "y"], name="new"))

# Test for renaming index using dict
result = df.rename_axis(index={"ll": "foo"})
assert result.index.names == ["foo", "nn"]

# Test for renaming index using a function
result = df.rename_axis(index=str.upper, axis=0)
assert result.index.names == ["LL", "NN"]

# Test for renaming index providing complete list
result = df.rename_axis(index=["foo", "goo"])
assert result.index.names == ["foo", "goo"]

# Test for changing index and columns at same time
sdf = df.reset_index().set_index("nn").drop(columns=["ll", "y"])
result = sdf.rename_axis(index="foo", columns="meh")
assert result.index.name == "foo"
assert result.columns.name == "meh"

# Test different error cases
with pytest.raises(TypeError, match="Must pass"):
    df.rename_axis(index="wrong")

with pytest.raises(ValueError, match="Length of names"):
    df.rename_axis(index=["wrong"])

with pytest.raises(TypeError, match="bogus"):
    df.rename_axis(bogus=None)
