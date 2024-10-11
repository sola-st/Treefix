# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_scalar.py
# GH 26989
# DataFrame.at and DataFrame.loc getter works with MultiIndex
df = DataFrame({"a": [1, 2]}, index=[[1, 2], [3, 4]])
assert df.index.nlevels == 2
assert df.at[(1, 3), "a"] == 1
assert df.loc[(1, 3), "a"] == 1

# Series.at and Series.loc getter works with MultiIndex
series = df["a"]
assert series.index.nlevels == 2
assert series.at[1, 3] == 1
assert series.loc[1, 3] == 1
