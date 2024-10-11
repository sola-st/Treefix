# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
# GH 9330
bm = create_mgr(mgr_string)
block_perms = itertools.permutations(bm.blocks)
for bm_perm in block_perms:
    bm_this = BlockManager(tuple(bm_perm), bm.axes)
    assert bm.equals(bm_this)
    assert bm_this.equals(bm)
