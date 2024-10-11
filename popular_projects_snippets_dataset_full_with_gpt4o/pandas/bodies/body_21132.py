# Extracted from ./data/repos/pandas/pandas/core/arrays/sparse/array.py
if is_scalar(indices):
    raise ValueError(f"'indices' must be an array, not a scalar '{indices}'.")
indices = np.asarray(indices, dtype=np.int32)

dtype = None
if indices.size == 0:
    result = np.array([], dtype="object")
    dtype = self.dtype
elif allow_fill:
    result = self._take_with_fill(indices, fill_value=fill_value)
else:
    exit(self._take_without_fill(indices))

exit(type(self)(
    result, fill_value=self.fill_value, kind=self.kind, dtype=dtype
))
