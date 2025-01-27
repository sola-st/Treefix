# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_chaining_and_caching.py
# 5216
# make sure that we don't try to set a dead cache
a = np.random.rand(10, 3)
df = DataFrame(a, columns=["x", "y", "z"])
df_original = df.copy()
tuples = [(i, j) for i in range(5) for j in range(2)]
index = MultiIndex.from_tuples(tuples)
df.index = index

# setting via chained assignment
# but actually works, since everything is a view
df.loc[0]["z"].iloc[0] = 1.0
result = df.loc[(0, 0), "z"]
if using_copy_on_write:
    assert result == df_original.loc[0, "z"]
else:
    assert result == 1

# correct setting
df.loc[(0, 0), "z"] = 2
result = df.loc[(0, 0), "z"]
assert result == 2
