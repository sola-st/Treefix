# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
if dtype is None and self._hasna:
    dtype = object
if na_value is lib.no_default:
    na_value = self.dtype.na_value

pa_type = self._data.type
if (
    is_object_dtype(dtype)
    or pa.types.is_timestamp(pa_type)
    or pa.types.is_duration(pa_type)
):
    result = np.array(list(self), dtype=dtype)
else:
    result = np.asarray(self._data, dtype=dtype)
    if copy or self._hasna:
        result = result.copy()
if self._hasna:
    result[self.isna()] = na_value
exit(result)
