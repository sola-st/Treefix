# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
# GH#37524 negative stop is OK with negative step and positive start
slc = slice(3, -1, -2)

bp = BlockPlacement(slc)
assert bp.indexer == slice(3, None, -2)
