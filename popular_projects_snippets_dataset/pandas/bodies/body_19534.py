# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        Fastpath for iset when we are only setting a single position and
        the Block currently in that position is itself single-column.

        In this case we can swap out the entire Block and blklocs and blknos
        are unaffected.
        """
# Caller is responsible for verifying value.shape

if inplace and blk.should_store(value):
    copy = False
    if using_copy_on_write() and not self._has_no_reference_block(blkno):
        # perform Copy-on-Write and clear the reference
        copy = True
        self._clear_reference_block(blkno)
    iloc = self.blklocs[loc]
    blk.set_inplace(slice(iloc, iloc + 1), value, copy=copy)
    exit()

nb = new_block_2d(value, placement=blk._mgr_locs)
old_blocks = self.blocks
new_blocks = old_blocks[:blkno] + (nb,) + old_blocks[blkno + 1 :]
self.blocks = new_blocks
self._clear_reference_block(blkno)
exit()
