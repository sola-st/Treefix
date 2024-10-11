# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
result = cls(data)
assert result.flags.allows_duplicate_labels is True

result = cls(data).set_flags(allows_duplicate_labels=False)
assert result.flags.allows_duplicate_labels is False
