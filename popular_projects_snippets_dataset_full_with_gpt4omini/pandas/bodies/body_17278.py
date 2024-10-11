# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
result = pd.concat(objs, **kwargs)
assert result.flags.allows_duplicate_labels is False
