# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
df = pd.DataFrame({"A": [1, 2]}).set_flags(allows_duplicate_labels=False)
assert df[["A"]].flags.allows_duplicate_labels is False
assert df["A"].flags.allows_duplicate_labels is False
assert df.loc[0].flags.allows_duplicate_labels is False
assert df.loc[[0]].flags.allows_duplicate_labels is False
assert df.loc[0, ["A"]].flags.allows_duplicate_labels is False
