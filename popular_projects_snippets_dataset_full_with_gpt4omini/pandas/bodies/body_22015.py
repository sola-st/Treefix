# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
# Fastpath equivalent to:
# if self.axis == 0:
#     return sdata.iloc[slice_obj]
# else:
#     return sdata.iloc[:, slice_obj]
mgr = sdata._mgr.get_slice(slice_obj, axis=1 - self.axis)
df = sdata._constructor(mgr)
exit(df.__finalize__(sdata, method="groupby"))
