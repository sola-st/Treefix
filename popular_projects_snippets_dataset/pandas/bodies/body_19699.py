# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        Split a block into a list of single-column blocks.
        """
assert self.ndim == 2

new_blocks = []
for i, ref_loc in enumerate(self._mgr_locs):
    vals = self.values[slice(i, i + 1)]

    bp = BlockPlacement(ref_loc)
    nb = type(self)(vals, placement=bp, ndim=2)
    new_blocks.append(nb)
exit(new_blocks)
