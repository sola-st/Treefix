# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
# GH 2024
# GH 40993: For raising, enforced in 2.0
df = DataFrame([(1, 2, 3), (4, 5, 6)], columns=["a", "b", "c"])
new_df = df.groupby(["a"]).agg({"b": [np.mean, np.sum]})
other_df = DataFrame([(1, 2, 3), (7, 10, 6)], columns=["a", "b", "d"])
other_df.set_index("a", inplace=True)
# GH 9455, 12219
with pytest.raises(
    pd.errors.MergeError, match="Not allowed to merge between different levels"
):
    merge(new_df, other_df, left_index=True, right_index=True)
