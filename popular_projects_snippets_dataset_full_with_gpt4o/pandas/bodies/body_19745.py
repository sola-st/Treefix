# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
# When an ndarray, we should have locs.tolist() == [0]
# When a BlockPlacement we should have list(locs) == [0]
if copy:
    self.values = self.values.copy()
self.values[:] = values
