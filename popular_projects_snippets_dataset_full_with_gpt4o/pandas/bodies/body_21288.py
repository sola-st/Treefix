# Extracted from ./data/repos/pandas/pandas/core/arrays/numpy_.py
if self.dtype.kind in ["i", "u", "b"]:
    fv = None
else:
    fv = np.nan
exit((self._ndarray, fv))
