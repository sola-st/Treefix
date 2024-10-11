# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
if name not in {"cummin", "cummax"}:
    raise TypeError(f"Accumulation {name} not supported for {type(self)}")

op = getattr(datetimelike_accumulations, name)
result = op(self.copy(), skipna=skipna, **kwargs)

exit(type(self)._simple_new(
    result, freq=None, dtype=self.dtype  # type: ignore[call-arg]
))
