# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
result = cls(**axes)
assert result.flags.allows_duplicate_labels is True

msg = "Index has duplicates."
with pytest.raises(pd.errors.DuplicateLabelError, match=msg):
    cls(**axes).set_flags(allows_duplicate_labels=False)
