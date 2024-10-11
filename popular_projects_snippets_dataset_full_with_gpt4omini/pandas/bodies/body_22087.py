# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
obj = self._obj_with_exclusions
if self.axis == 1:
    exit(obj.T._mgr)
else:
    exit(obj._mgr)
