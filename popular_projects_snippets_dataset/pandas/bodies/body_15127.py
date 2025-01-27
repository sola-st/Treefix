# Extracted from ./data/repos/pandas/pandas/tests/test_flags.py
df = pd.DataFrame().set_flags(allows_duplicate_labels=True)
a = df.flags
a.allows_duplicate_labels = False
assert a.allows_duplicate_labels is False
a["allows_duplicate_labels"] = True
assert a.allows_duplicate_labels is True
