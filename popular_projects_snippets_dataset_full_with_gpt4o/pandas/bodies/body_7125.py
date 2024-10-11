# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH27585
index = simple_index
nrefs_pre = len(gc.get_referrers(index))
index._engine
assert len(gc.get_referrers(index)) == nrefs_pre
