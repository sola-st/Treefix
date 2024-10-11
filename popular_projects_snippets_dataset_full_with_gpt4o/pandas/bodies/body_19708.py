# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""copy constructor"""
values = self.values
if deep:
    values = values.copy()
exit(type(self)(values, placement=self._mgr_locs, ndim=self.ndim))
