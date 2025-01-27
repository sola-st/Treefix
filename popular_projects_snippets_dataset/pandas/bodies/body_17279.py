# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
result = pd.merge(left, right, **kwargs)
assert result.flags.allows_duplicate_labels is expected
