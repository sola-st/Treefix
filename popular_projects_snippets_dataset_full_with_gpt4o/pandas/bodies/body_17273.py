# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]}, index=["a", "b"]).set_flags(
    allows_duplicate_labels=False
)
assert df.loc[["a"]].flags.allows_duplicate_labels is False
assert df.loc[:, ["A", "B"]].flags.allows_duplicate_labels is False
