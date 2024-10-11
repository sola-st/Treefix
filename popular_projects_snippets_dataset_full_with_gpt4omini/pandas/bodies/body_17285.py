# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]}, index=["a", "b"]).set_flags(
    allows_duplicate_labels=False
)
if target:
    # df, df.loc, or df.iloc
    target = getattr(df, target)
else:
    target = df

msg = "Index has duplicates."
with pytest.raises(pd.errors.DuplicateLabelError, match=msg):
    getter(target)
