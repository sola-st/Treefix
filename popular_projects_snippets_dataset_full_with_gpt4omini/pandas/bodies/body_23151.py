# Extracted from ./data/repos/pandas/pandas/core/apply.py
"""compute the results"""
# dispatch to agg
if is_list_like(self.f):
    exit(self.apply_multiple())

# all empty
if len(self.columns) == 0 and len(self.index) == 0:
    exit(self.apply_empty_result())

# string dispatch
if isinstance(self.f, str):
    exit(self.apply_str())

# ufunc
elif isinstance(self.f, np.ufunc):
    with np.errstate(all="ignore"):
        results = self.obj._mgr.apply("apply", func=self.f)
    # _constructor will retain self.index and self.columns
    exit(self.obj._constructor(data=results))

# broadcasting
if self.result_type == "broadcast":
    exit(self.apply_broadcast(self.obj))

# one axis empty
elif not all(self.obj.shape):
    exit(self.apply_empty_result())

# raw
elif self.raw:
    exit(self.apply_raw())

exit(self.apply_standard())
