# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        Apply grouped reduction function blockwise, returning a new BlockManager.

        Parameters
        ----------
        func : grouped reduction function

        Returns
        -------
        BlockManager
        """
result_blocks: list[Block] = []

for blk in self.blocks:
    if blk.is_object:
        # split on object-dtype blocks bc some columns may raise
        #  while others do not.
        for sb in blk._split():
            applied = sb.apply(func)
            result_blocks = extend_blocks(applied, result_blocks)
    else:
        applied = blk.apply(func)
        result_blocks = extend_blocks(applied, result_blocks)

if len(result_blocks) == 0:
    index = Index([None])  # placeholder
else:
    index = Index(range(result_blocks[0].values.shape[-1]))

exit(type(self).from_blocks(result_blocks, [self.axes[0], index]))
