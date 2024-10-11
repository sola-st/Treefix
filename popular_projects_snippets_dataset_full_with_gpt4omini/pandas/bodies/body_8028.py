# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_base.py
index = simple_index
key = index[0]
assert index._can_hold_identifiers_and_holds_name(key) is True
