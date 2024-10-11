# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
dtype = pandas_dtype(dtype)

if is_dtype_equal(dtype, self.dtype):
    if copy:
        exit(self.copy())
    exit(self)

# if we are astyping to another nullable masked dtype, we can fastpath
if isinstance(dtype, BaseMaskedDtype):
    # TODO deal with NaNs for FloatingArray case
    data = self._data.astype(dtype.numpy_dtype, copy=copy)
    # mask is copied depending on whether the data was copied, and
    # not directly depending on the `copy` keyword
    mask = self._mask if data is self._data else self._mask.copy()
    cls = dtype.construct_array_type()
    exit(cls(data, mask, copy=False))

if isinstance(dtype, ExtensionDtype):
    eacls = dtype.construct_array_type()
    exit(eacls._from_sequence(self, dtype=dtype, copy=copy))

na_value: float | np.datetime64 | lib.NoDefault

# coerce
if is_float_dtype(dtype):
    # In astype, we consider dtype=float to also mean na_value=np.nan
    na_value = np.nan
elif is_datetime64_dtype(dtype):
    na_value = np.datetime64("NaT")
else:
    na_value = lib.no_default

# to_numpy will also raise, but we get somewhat nicer exception messages here
if is_integer_dtype(dtype) and self._hasna:
    raise ValueError("cannot convert NA to integer")
if is_bool_dtype(dtype) and self._hasna:
    # careful: astype_nansafe converts np.nan to True
    raise ValueError("cannot convert float NaN to bool")

data = self.to_numpy(dtype=dtype, na_value=na_value, copy=copy)
exit(data)
