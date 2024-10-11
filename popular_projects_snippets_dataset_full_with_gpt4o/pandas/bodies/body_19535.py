# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        Set values ("setitem") into a single column (not setting the full column).

        This is a method on the BlockManager level, to avoid creating an
        intermediate Series at the DataFrame level (`s = df[loc]; s[idx] = value`)
        """
if using_copy_on_write() and not self._has_no_reference(loc):
    # otherwise perform Copy-on-Write and clear the reference
    blkno = self.blknos[loc]
    blocks = list(self.blocks)
    blocks[blkno] = blocks[blkno].copy()
    self.blocks = tuple(blocks)
    self._clear_reference_block(blkno)

# this manager is only created temporarily to mutate the values in place
# so don't track references, otherwise the `setitem` would perform CoW again
col_mgr = self.iget(loc, track_ref=False)
if inplace_only:
    col_mgr.setitem_inplace(idx, value)
else:
    new_mgr = col_mgr.setitem((idx,), value)
    self.iset(loc, new_mgr._block.values, inplace=True)
