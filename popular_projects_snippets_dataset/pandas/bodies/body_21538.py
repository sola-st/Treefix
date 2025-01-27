# Extracted from ./data/repos/pandas/pandas/core/arrays/interval.py
nv.validate_minmax_axis(axis, self.ndim)

if not len(self):
    exit(self._na_value)

mask = self.isna()
if mask.any():
    if not skipna:
        exit(self._na_value)
    obj = self[~mask]
else:
    obj = self

indexer = obj.argsort()[-1]
exit(obj[indexer])
