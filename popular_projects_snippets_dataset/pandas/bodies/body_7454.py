# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_setops.py
# GH 15270
assert not idx.empty
assert idx[:0].empty
