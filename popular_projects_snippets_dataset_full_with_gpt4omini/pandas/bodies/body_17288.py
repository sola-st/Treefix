# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
msg = "Index has duplicates."
with pytest.raises(pd.errors.DuplicateLabelError, match=msg):
    pd.Series(1, index=idx).set_flags(allows_duplicate_labels=False)

with pytest.raises(pd.errors.DuplicateLabelError, match=msg):
    pd.DataFrame({"A": [1, 1]}, index=idx).set_flags(allows_duplicate_labels=False)

with pytest.raises(pd.errors.DuplicateLabelError, match=msg):
    pd.DataFrame([[1, 2]], columns=idx).set_flags(allows_duplicate_labels=False)
