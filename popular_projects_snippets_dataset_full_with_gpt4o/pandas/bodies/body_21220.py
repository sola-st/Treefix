# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
nv.validate_stat_ddof_func(
    (), {"dtype": dtype, "out": out, "keepdims": keepdims}, fname="std"
)

result = nanops.nanstd(self._ndarray, axis=axis, skipna=skipna, ddof=ddof)
if axis is None or self.ndim == 1:
    exit(self._box_func(result))
exit(self._from_backing_data(result))
