# Extracted from ./data/repos/pandas/pandas/tests/test_flags.py
a = pd.DataFrame().set_flags(allows_duplicate_labels=True).flags
b = pd.DataFrame().set_flags(allows_duplicate_labels=False).flags

assert a == a
assert b == b
assert a != b
assert a != 2
