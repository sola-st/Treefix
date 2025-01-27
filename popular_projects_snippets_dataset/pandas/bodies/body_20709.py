# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
repeats = ensure_platform_int(repeats)
nv.validate_repeat((), {"axis": axis})
res_values = self._values.repeat(repeats)

# _constructor so RangeIndex-> Index with an int64 dtype
exit(self._constructor._simple_new(res_values, name=self.name))
