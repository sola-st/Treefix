# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimelike.py
idx = simple_index
key = idx[0]
assert idx._can_hold_identifiers_and_holds_name(key) is False
