# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_counting.py
np.random.seed(0)
df = DataFrame({"a": np.random.choice(list("abcdef"), 100)})
g = df.groupby("a", sort=sort)
df["group_id"] = -1
df["group_index"] = -1

for i, (_, group) in enumerate(g):
    df.loc[group.index, "group_id"] = i
    for j, ind in enumerate(group.index):
        df.loc[ind, "group_index"] = j

tm.assert_series_equal(Series(df["group_id"].values), g.ngroup())
tm.assert_series_equal(Series(df["group_index"].values), g.cumcount())
