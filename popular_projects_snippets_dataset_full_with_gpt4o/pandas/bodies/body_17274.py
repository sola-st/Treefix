# Extracted from ./data/repos/pandas/pandas/tests/generic/test_duplicate_labels.py
ser = pd.Series(dtype=float).set_flags(allows_duplicate_labels=False)
assert ser.to_frame().flags.allows_duplicate_labels is False
