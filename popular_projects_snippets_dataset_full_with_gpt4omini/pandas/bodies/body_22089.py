# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
if not self.as_index:
    # GH 41998 - empty mgr always gets index of length 0
    rows = mgr.shape[1] if mgr.shape[0] > 0 else 0
    index = Index(range(rows))
    mgr.set_axis(1, index)
    result = self.obj._constructor(mgr)

    result = self._insert_inaxis_grouper(result)
    result = result._consolidate()
else:
    index = self.grouper.result_index
    mgr.set_axis(1, index)
    result = self.obj._constructor(mgr)

if self.axis == 1:
    result = result.T

# Note: we really only care about inferring numeric dtypes here
exit(self._reindex_output(result).infer_objects(copy=False))
