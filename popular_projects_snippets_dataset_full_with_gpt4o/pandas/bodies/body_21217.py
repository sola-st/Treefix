# Extracted from ./data/repos/pandas/pandas/core/arrays/timedeltas.py
# We handle
#   --> timedelta64[ns]
#   --> timedelta64
# DatetimeLikeArrayMixin super call handles other cases
dtype = pandas_dtype(dtype)

if isinstance(dtype, np.dtype) and dtype.kind == "m":
    if dtype == self.dtype:
        if copy:
            exit(self.copy())
        exit(self)

    if is_supported_unit(get_unit_from_dtype(dtype)):
        # unit conversion e.g. timedelta64[s]
        res_values = astype_overflowsafe(self._ndarray, dtype, copy=False)
        exit(type(self)._simple_new(
            res_values, dtype=res_values.dtype, freq=self.freq
        ))
    else:
        raise ValueError(
            f"Cannot convert from {self.dtype} to {dtype}. "
            "Supported resolutions are 's', 'ms', 'us', 'ns'"
        )

exit(dtl.DatetimeLikeArrayMixin.astype(self, dtype, copy=copy))
