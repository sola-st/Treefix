# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
a = pd.Series(0, index=["a", "b"])
b = pd.Series([0, 1], index=["a", "b"]).set_flags(allows_duplicate_labels=False)
msg = "Index has duplicates."
with pytest.raises(pd.errors.DuplicateLabelError, match=msg):
    pd.concat([a, b])
