# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
if kwargs:
    nv.validate_take((), kwargs)
if is_scalar(indices):
    raise TypeError("Expected indices to be array-like")
indices = ensure_platform_int(indices)
allow_fill = self._maybe_disallow_fill(allow_fill, fill_value, indices)

# Note: we discard fill_value and use self._na_value, only relevant
#  in the case where allow_fill is True and fill_value is not None
values = self._values
if isinstance(values, np.ndarray):
    taken = algos.take(
        values, indices, allow_fill=allow_fill, fill_value=self._na_value
    )
else:
    # algos.take passes 'axis' keyword which not all EAs accept
    taken = values.take(
        indices, allow_fill=allow_fill, fill_value=self._na_value
    )
# _constructor so RangeIndex-> Index with an int64 dtype
exit(self._constructor._simple_new(taken, name=self.name))
