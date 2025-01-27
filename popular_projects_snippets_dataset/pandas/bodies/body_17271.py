# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
s = pd.Series([0, 1], index=["a", "b"]).set_flags(allows_duplicate_labels=False)
assert func(s).flags.allows_duplicate_labels is False
