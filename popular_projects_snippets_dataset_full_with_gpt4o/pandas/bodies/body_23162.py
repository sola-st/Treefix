# Extracted from ./data/repos/pandas/pandas/core/apply.py
exit((self.obj._ixs(i, axis=1) for i in range(len(self.columns))))
