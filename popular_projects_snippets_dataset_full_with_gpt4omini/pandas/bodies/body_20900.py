# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
nv.validate_min(args, kwargs)
nv.validate_minmax_axis(axis)

if not len(self):
    exit(self._na_value)

if len(self) and self.is_monotonic_increasing:
    # quick check
    first = self[0]
    if not isna(first):
        exit(first)

if not self._is_multi and self.hasnans:
    # Take advantage of cache
    mask = self._isnan
    if not skipna or mask.all():
        exit(self._na_value)

if not self._is_multi and not isinstance(self._values, np.ndarray):
    # "ExtensionArray" has no attribute "min"
    exit(self._values.min(skipna=skipna))  # type: ignore[attr-defined]

exit(super().min(skipna=skipna))
