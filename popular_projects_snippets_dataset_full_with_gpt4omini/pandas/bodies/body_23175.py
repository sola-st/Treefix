# Extracted from ./data/repos/pandas/pandas/core/apply.py
obj = self.obj
exit(obj._constructor(dtype=obj.dtype, index=obj.index).__finalize__(
    obj, method="apply"
))
