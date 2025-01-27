# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
if mgr.ndim == 1:
    mgr = cast(SingleManager, mgr)
    single = mgr
else:
    mgr = cast(Manager2D, mgr)
    single = mgr.iget(0)
ser = self.obj._constructor(single, name=self.obj.name)
# NB: caller is responsible for setting ser.index
exit(ser)
