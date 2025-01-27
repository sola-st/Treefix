# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_integrity.py
key = idx[0]
assert idx._can_hold_identifiers_and_holds_name(key) is True
