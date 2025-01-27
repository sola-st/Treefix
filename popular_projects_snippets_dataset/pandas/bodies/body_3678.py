# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_isin.py
df1 = DataFrame({"A": [1, 2, 3, 4], "B": [2, np.nan, 4, 4]})
# just cols duped
df2 = DataFrame([[0, 2], [12, 4], [2, np.nan], [4, 5]], columns=["B", "B"])
msg = r"cannot compute isin with a duplicate axis\."
with pytest.raises(ValueError, match=msg):
    df1.isin(df2)

# just index duped
df2 = DataFrame(
    [[0, 2], [12, 4], [2, np.nan], [4, 5]],
    columns=["A", "B"],
    index=[0, 0, 1, 1],
)
with pytest.raises(ValueError, match=msg):
    df1.isin(df2)

# cols and index:
df2.columns = ["B", "B"]
with pytest.raises(ValueError, match=msg):
    df1.isin(df2)
