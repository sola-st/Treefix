# Extracted from ./data/repos/pandas/pandas/tests/test_flags.py
a = repr(pd.DataFrame({"A"}).set_flags(allows_duplicate_labels=True).flags)
assert a == "<Flags(allows_duplicate_labels=True)>"
a = repr(pd.DataFrame({"A"}).set_flags(allows_duplicate_labels=False).flags)
assert a == "<Flags(allows_duplicate_labels=False)>"
