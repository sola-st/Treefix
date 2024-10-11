# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
mgr = create_mgr("a: sparse-1; b: sparse-2; c: f8")
assert len(mgr.blocks) == 3
assert isinstance(mgr, BlockManager)
