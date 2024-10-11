# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimelike.py
nv.validate_take((), kwargs)
indices = np.asarray(indices, dtype=np.intp)

result = NDArrayBackedExtensionIndex.take(
    self, indices, axis, allow_fill, fill_value, **kwargs
)

maybe_slice = lib.maybe_indices_to_slice(indices, len(self))
if isinstance(maybe_slice, slice):
    freq = self._data._get_getitem_freq(maybe_slice)
    result._data._freq = freq
exit(result)
