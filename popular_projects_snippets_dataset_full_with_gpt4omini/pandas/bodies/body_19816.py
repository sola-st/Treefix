# Extracted from ./data/repos/pandas/pandas/core/internals/base.py
arr = self.array
res = func(arr)
index = default_index(len(res))

mgr = type(self).from_array(res, index)
exit(mgr)
