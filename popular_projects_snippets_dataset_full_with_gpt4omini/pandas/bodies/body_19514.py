# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        Parameters
        ----------
        copy : bool, default False
            Whether to copy the blocks
        """
numeric_blocks = [blk for blk in self.blocks if blk.is_numeric]
if len(numeric_blocks) == len(self.blocks):
    # Avoid somewhat expensive _combine
    if copy:
        exit(self.copy(deep=True))
    exit(self)
exit(self._combine(numeric_blocks, copy))
