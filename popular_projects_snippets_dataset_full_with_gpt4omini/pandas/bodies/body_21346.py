# Extracted from ./data/repos/pandas/pandas/core/arrays/_mixins.py
# (for now) when self.ndim == 2, we assume axis=0
func = missing.get_fill_func(method, ndim=self.ndim)
func(self._ndarray.T, limit=limit, mask=mask.T)
