# Extracted from ./data/repos/pandas/pandas/core/reshape/concat.py
if self._is_series and self.bm_axis == 1:
    exit(2)
else:
    exit(self.objs[0].ndim)
