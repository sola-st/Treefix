# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
tmp_mgr = create_mgr("a:bool; a: f8")

axes, blocks = tmp_mgr.axes, tmp_mgr.blocks

blocks[0].mgr_locs = BlockPlacement(np.array([0]))
blocks[1].mgr_locs = BlockPlacement(np.array([0]))

# test trying to create block manager with overlapping ref locs

msg = "Gaps in blk ref_locs"

with pytest.raises(AssertionError, match=msg):
    mgr = BlockManager(blocks, axes)
    mgr._rebuild_blknos_and_blklocs()

blocks[0].mgr_locs = BlockPlacement(np.array([0]))
blocks[1].mgr_locs = BlockPlacement(np.array([1]))
mgr = BlockManager(blocks, axes)
mgr.iget(1)
