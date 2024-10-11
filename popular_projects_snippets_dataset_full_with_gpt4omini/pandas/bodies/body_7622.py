# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_indexing.py
assert ("foo", "two") in idx
assert ("bar", "two") not in idx
assert None not in idx
