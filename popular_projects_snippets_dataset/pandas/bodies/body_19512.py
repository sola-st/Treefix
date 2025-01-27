# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
blocks = [blk for blk in self.blocks if predicate(blk.values)]
exit(self._combine(blocks, copy=False))
