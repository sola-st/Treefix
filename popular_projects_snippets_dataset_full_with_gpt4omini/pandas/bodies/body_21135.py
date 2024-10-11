# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py

msg = "searchsorted requires high memory usage."
warnings.warn(msg, PerformanceWarning, stacklevel=find_stack_level())
if not is_scalar(v):
    v = np.asarray(v)
v = np.asarray(v)
exit(np.asarray(self, dtype=self.dtype.subtype).searchsorted(v, side, sorter))
