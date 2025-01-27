# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
# only reached with self.ndim == 2 and axis == 1
axis = self._normalize_axis(axis)
exit(self.apply("diff", n=n, axis=axis))
