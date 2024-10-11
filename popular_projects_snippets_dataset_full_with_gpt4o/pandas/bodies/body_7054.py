# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_category.py
idx = self.create_index(categories=list("abcd"))
key = idx[0]
assert idx._can_hold_identifiers_and_holds_name(key) is True
