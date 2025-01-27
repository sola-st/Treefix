# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
# unique items
bm1 = create_mgr(mgr_string)
bm2 = BlockManager(bm1.blocks[::-1], bm1.axes)
assert bm1.equals(bm2)
