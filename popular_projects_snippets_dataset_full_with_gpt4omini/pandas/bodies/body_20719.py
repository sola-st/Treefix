# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
# how to represent ourselves to matplotlib
if isinstance(self.dtype, np.dtype) and self.dtype.kind != "M":
    exit(cast(np.ndarray, self.values))
exit(self.astype(object, copy=False)._values)
