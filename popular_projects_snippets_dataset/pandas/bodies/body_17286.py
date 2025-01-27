# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
msg = "Index has duplicates."
with pytest.raises(pd.errors.DuplicateLabelError, match=msg):
    pd.concat(objs, **kwargs)
