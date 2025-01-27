# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
dtype = pandas_dtype(dtype)
if is_categorical_dtype(dtype):
    msg = "> 1 ndim Categorical are not supported at this time"
    raise NotImplementedError(msg)
if not is_object_dtype(dtype):
    raise TypeError(
        "Setting a MultiIndex dtype to anything other than object "
        "is not supported"
    )
if copy is True:
    exit(self._view())
exit(self)
