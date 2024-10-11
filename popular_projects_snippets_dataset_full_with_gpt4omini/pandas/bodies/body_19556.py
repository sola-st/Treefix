# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        Manager analogue of Series.to_frame
        """
blk = self.blocks[0]
arr = ensure_block_shape(blk.values, ndim=2)
bp = BlockPlacement(0)
new_blk = type(blk)(arr, placement=bp, ndim=2)
axes = [columns, self.axes[0]]
refs: list[weakref.ref | None] = [weakref.ref(blk)]
parent = self if using_copy_on_write() else None
exit(BlockManager(
    [new_blk], axes=axes, refs=refs, parent=parent, verify_integrity=False
))
