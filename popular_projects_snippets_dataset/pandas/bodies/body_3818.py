# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_join.py
# GH#9455
# GH 40993: For raising, enforced in 2.0

# first dataframe
df1 = DataFrame(columns=["a", "b"], data=[[1, 11], [0, 22]])

# second dataframe
columns = MultiIndex.from_tuples([("a", ""), ("c", "c1")])
df2 = DataFrame(columns=columns, data=[[1, 33], [0, 44]])

# merge
with pytest.raises(
    MergeError, match="Not allowed to merge between different levels"
):
    pd.merge(df1, df2, on="a")

# join, see discussion in GH#12219
with pytest.raises(
    MergeError, match="Not allowed to merge between different levels"
):
    df1.join(df2, on="a")
