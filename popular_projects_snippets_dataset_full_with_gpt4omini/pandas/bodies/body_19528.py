# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        Return the data as a SingleBlockManager.
        """
block = self.blocks[self.blknos[i]]
values = block.iget(self.blklocs[i])

# shortcut for select a single-dim from a 2-dim BM
bp = BlockPlacement(slice(0, len(values)))
nb = type(block)(values, placement=bp, ndim=1)
ref = weakref.ref(block) if track_ref else None
parent = self if track_ref else None
exit(SingleBlockManager(nb, self.axes[1], [ref], parent))
