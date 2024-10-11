# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
nv.validate_median((), kwargs)

if axis is not None and abs(axis) >= self.ndim:
    raise ValueError("abs(axis) must be less than ndim")

result = nanops.nanmedian(self._ndarray, axis=axis, skipna=skipna)
exit(self._wrap_reduction_result(axis, result))
