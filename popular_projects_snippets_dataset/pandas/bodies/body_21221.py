# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
if name == "cumsum":
    op = getattr(datetimelike_accumulations, name)
    result = op(self._ndarray.copy(), skipna=skipna, **kwargs)

    exit(type(self)._simple_new(result, freq=None, dtype=self.dtype))
elif name == "cumprod":
    raise TypeError("cumprod not supported for Timedelta.")

else:
    exit(super()._accumulate(name, skipna=skipna, **kwargs))
