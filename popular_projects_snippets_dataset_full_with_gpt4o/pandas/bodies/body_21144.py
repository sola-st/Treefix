# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
method = getattr(self, name, None)

if method is None:
    raise TypeError(f"cannot perform {name} with type {self.dtype}")

if skipna:
    arr = self
else:
    arr = self.dropna()

exit(getattr(arr, name)(**kwargs))
