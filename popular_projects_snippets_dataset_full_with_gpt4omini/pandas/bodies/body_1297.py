# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_categorical.py
# Setting-with-expansion with a new key "d" that is not among caegories
df.loc["a"] = 20

# Setting a new row on an existing column
df3 = df.copy()
df3.loc["d", "A"] = 10
bidx3 = Index(list("aabbcad"), name="B")
expected3 = DataFrame(
    {
        "A": [20, 20, 2, 3, 4, 20, 10.0],
    },
    index=Index(bidx3),
)
tm.assert_frame_equal(df3, expected3)

# Settig a new row _and_ new column
df4 = df.copy()
df4.loc["d", "C"] = 10
expected3 = DataFrame(
    {
        "A": [20, 20, 2, 3, 4, 20, np.nan],
        "C": [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 10],
    },
    index=Index(bidx3),
)
tm.assert_frame_equal(df4, expected3)
