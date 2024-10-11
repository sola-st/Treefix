# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
nv.validate_repeat((), {"axis": axis})
ind = np.arange(len(self)).repeat(repeats)
exit(self.take(ind))
