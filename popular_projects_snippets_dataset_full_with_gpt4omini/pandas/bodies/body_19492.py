# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
dtypes = np.array([blk.dtype for blk in self.blocks])
exit(dtypes.take(self.blknos))
