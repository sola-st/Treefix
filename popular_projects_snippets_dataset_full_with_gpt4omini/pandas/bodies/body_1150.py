# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH#41369
df = DataFrame(
    {"a": 1.0, "b": 2}, index=MultiIndex.from_arrays([[3], [4]], names=["c", "d"])
)
result = df.loc[(3, 4), "b"]
assert result == 2
assert isinstance(result, np.int64)
result = df.loc[[(3, 4)], "b"].iloc[0]
assert result == 2
assert isinstance(result, np.int64)
