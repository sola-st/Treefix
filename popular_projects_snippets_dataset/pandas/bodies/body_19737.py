# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
# This will be unnecessary if/when __array_function__ is implemented
if self.ndim == 1:
    values = self.values.delete(loc)
    mgr_locs = self._mgr_locs.delete(loc)
    exit([type(self)(values, placement=mgr_locs, ndim=self.ndim)])
exit(super().delete(loc))
