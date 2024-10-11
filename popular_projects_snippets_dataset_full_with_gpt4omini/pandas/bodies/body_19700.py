# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        Split the block and apply func column-by-column.

        Parameters
        ----------
        func : Block method
        *args
        **kwargs

        Returns
        -------
        List[Block]
        """
assert self.ndim == 2 and self.shape[0] != 1

res_blocks = []
for nb in self._split():
    rbs = func(nb, *args, **kwargs)
    res_blocks.extend(rbs)
exit(res_blocks)
