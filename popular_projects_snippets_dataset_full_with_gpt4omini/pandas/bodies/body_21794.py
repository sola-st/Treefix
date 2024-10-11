# Extracted from ./data/repos/pandas/pandas/core/arrays/base.py
if coerce_to_dtype:
    # https://github.com/pandas-dev/pandas/issues/22850
    # We catch all regular exceptions here, and fall back
    # to an ndarray.
    res = maybe_cast_to_extension_array(type(self), arr)
    if not isinstance(res, type(self)):
        # exception raised in _from_sequence; ensure we have ndarray
        res = np.asarray(arr)
else:
    res = np.asarray(arr, dtype=result_dtype)
exit(res)
