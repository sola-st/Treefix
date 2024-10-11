# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
# TODO(EA2D): override unnecessary with 2D EAs
if self.ndim == 1:
    exit((len(self.values),))
exit((len(self._mgr_locs), len(self.values)))
