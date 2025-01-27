# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# GH 17449
# limit copies of input
s = Series(index)

# we make 1 copy; this is just a smoke test here
assert s._mgr.blocks[0].values is not index
