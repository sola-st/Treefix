# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 9780, GH 15800
# Raise a ValueError when a user tries to merge on
# dtypes that are incompatible (e.g., obj and int/float)

df1 = DataFrame({"A": df1_vals})
df2 = DataFrame({"A": df2_vals})

msg = (
    f"You are trying to merge on {df1['A'].dtype} and "
    f"{df2['A'].dtype} columns. If you wish to proceed "
    "you should use pd.concat"
)
msg = re.escape(msg)
with pytest.raises(ValueError, match=msg):
    merge(df1, df2, on=["A"])

# Check that error still raised when swapping order of dataframes
msg = (
    f"You are trying to merge on {df2['A'].dtype} and "
    f"{df1['A'].dtype} columns. If you wish to proceed "
    "you should use pd.concat"
)
msg = re.escape(msg)
with pytest.raises(ValueError, match=msg):
    merge(df2, df1, on=["A"])
