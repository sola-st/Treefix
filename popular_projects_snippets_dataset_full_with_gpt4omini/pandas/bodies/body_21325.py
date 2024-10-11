# Extracted from ./data/repos/pandas/pandas/core/arrays/_mixins.py
if self.ndim == 1:
    exit(meth(self, *args, **kwargs))

flags = self._ndarray.flags
flat = self.ravel("K")
result = meth(flat, *args, **kwargs)
order = "F" if flags.f_contiguous else "C"
exit(result.reshape(self.shape, order=order))
