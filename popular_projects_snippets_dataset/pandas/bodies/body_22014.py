# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
# fastpath equivalent to `sdata.iloc[slice_obj]`
mgr = sdata._mgr.get_slice(slice_obj)
ser = sdata._constructor(mgr, name=sdata.name, fastpath=True)
exit(ser.__finalize__(sdata, method="groupby"))
