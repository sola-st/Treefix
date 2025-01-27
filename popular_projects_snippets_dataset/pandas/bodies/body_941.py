# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_scalar.py
# GH 26989
# DataFrame.at and DataFrame.loc setter works with MultiIndex
df = DataFrame({"a": [1, 2]}, index=[[1, 2], [3, 4]])
assert df.index.nlevels == 2
df.at[(1, 3), "a"] = 3
assert df.at[(1, 3), "a"] == 3
df.loc[(1, 3), "a"] = 4
assert df.loc[(1, 3), "a"] == 4

# Series.at and Series.loc setter works with MultiIndex
series = df["a"]
assert series.index.nlevels == 2
series.at[1, 3] = 5
assert series.at[1, 3] == 5
series.loc[1, 3] = 6
assert series.loc[1, 3] == 6
