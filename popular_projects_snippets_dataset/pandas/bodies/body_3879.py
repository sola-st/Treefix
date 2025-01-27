# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py

# GH #9746: fill_value keyword argument for Series
# and DataFrame unstack

# From a series
data = Series([1, 2, 4, 5], dtype=np.int16)
data.index = MultiIndex.from_tuples(
    [("x", "a"), ("x", "b"), ("y", "b"), ("z", "a")]
)

result = data.unstack(fill_value=-1)
expected = DataFrame(
    {"a": [1, -1, 5], "b": [2, 4, -1]}, index=["x", "y", "z"], dtype=np.int16
)
tm.assert_frame_equal(result, expected)

# From a series with incorrect data type for fill_value
result = data.unstack(fill_value=0.5)
expected = DataFrame(
    {"a": [1, 0.5, 5], "b": [2, 4, 0.5]}, index=["x", "y", "z"], dtype=float
)
tm.assert_frame_equal(result, expected)

# GH #13971: fill_value when unstacking multiple levels:
df = DataFrame(
    {"x": ["a", "a", "b"], "y": ["j", "k", "j"], "z": [0, 1, 2], "w": [0, 1, 2]}
).set_index(["x", "y", "z"])
unstacked = df.unstack(["x", "y"], fill_value=0)
key = ("w", "b", "j")
expected = unstacked[key]
result = Series([0, 0, 2], index=unstacked.index, name=key)
tm.assert_series_equal(result, expected)

stacked = unstacked.stack(["x", "y"])
stacked.index = stacked.index.reorder_levels(df.index.names)
# Workaround for GH #17886 (unnecessarily casts to float):
stacked = stacked.astype(np.int64)
result = stacked.loc[df.index]
tm.assert_frame_equal(result, df)

# From a series
s = df["w"]
result = s.unstack(["x", "y"], fill_value=0)
expected = unstacked["w"]
tm.assert_frame_equal(result, expected)
