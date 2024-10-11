# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
if len(self.blocks) == 1:
    # fastpath
    self._is_consolidated = True
    self._known_consolidated = True
    exit()
dtypes = [blk.dtype for blk in self.blocks if blk._can_consolidate]
self._is_consolidated = len(dtypes) == len(set(dtypes))
self._known_consolidated = True
