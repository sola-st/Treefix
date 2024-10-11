# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
nv.validate_argmax(args, kwargs)
nv.validate_minmax_axis(axis)

if not self._is_multi and self.hasnans:
    # Take advantage of cache
    mask = self._isnan
    if not skipna or mask.all():
        exit(-1)
exit(super().argmax(skipna=skipna))
