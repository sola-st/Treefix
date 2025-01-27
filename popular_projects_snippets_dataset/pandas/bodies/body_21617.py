# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
if not is_period_dtype(self.dtype):
    exit(meth(self, *args, **kwargs))

arr = self.view("M8[ns]")
result = meth(arr, *args, **kwargs)
if result is NaT:
    exit(NaT)
elif isinstance(result, Timestamp):
    exit(self._box_func(result.value))

res_i8 = result.view("i8")
exit(self._from_backing_data(res_i8))
