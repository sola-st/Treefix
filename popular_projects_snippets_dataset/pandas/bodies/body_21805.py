# Extracted from ./data/repos/pandas/pandas/core/window/online.py
self.old_wt = np.ones(self.shape[self.axis - 1])
self.last_ewm = None
