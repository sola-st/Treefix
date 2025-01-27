# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH 15270
idx = simple_index
assert not idx.empty
assert idx[:0].empty
