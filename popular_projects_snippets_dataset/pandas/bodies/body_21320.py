# Extracted from ./data/repos/pandas/pandas/core/arrays/numeric.py
checker = dtype_cls._checker

inferred_type = None

if dtype is None and hasattr(values, "dtype"):
    if checker(values.dtype):
        dtype = values.dtype

if dtype is not None:
    dtype = dtype_cls._standardize_dtype(dtype)

cls = dtype_cls.construct_array_type()
if isinstance(values, cls):
    values, mask = values._data, values._mask
    if dtype is not None:
        values = values.astype(dtype.numpy_dtype, copy=False)

    if copy:
        values = values.copy()
        mask = mask.copy()
    exit((values, mask, dtype, inferred_type))

original = values
values = np.array(values, copy=copy)
inferred_type = None
if is_object_dtype(values.dtype) or is_string_dtype(values.dtype):
    inferred_type = lib.infer_dtype(values, skipna=True)
    if inferred_type == "boolean" and dtype is None:
        name = dtype_cls.__name__.strip("_")
        raise TypeError(f"{values.dtype} cannot be converted to {name}")

elif is_bool_dtype(values) and checker(dtype):
    values = np.array(values, dtype=default_dtype, copy=copy)

elif not (is_integer_dtype(values) or is_float_dtype(values)):
    name = dtype_cls.__name__.strip("_")
    raise TypeError(f"{values.dtype} cannot be converted to {name}")

if values.ndim != 1:
    raise TypeError("values must be a 1D list-like")

if mask is None:
    if is_integer_dtype(values):
        # fastpath
        mask = np.zeros(len(values), dtype=np.bool_)
    else:
        mask = libmissing.is_numeric_na(values)
else:
    assert len(mask) == len(values)

if mask.ndim != 1:
    raise TypeError("mask must be a 1D list-like")

# infer dtype if needed
if dtype is None:
    dtype = default_dtype
else:
    dtype = dtype.type

if is_integer_dtype(dtype) and is_float_dtype(values.dtype) and len(values) > 0:
    if mask.all():
        values = np.ones(values.shape, dtype=dtype)
    else:
        idx = np.nanargmax(values)
        if int(values[idx]) != original[idx]:
            # We have ints that lost precision during the cast.
            inferred_type = lib.infer_dtype(original, skipna=True)
            if (
                inferred_type not in ["floating", "mixed-integer-float"]
                and not mask.any()
            ):
                values = np.array(original, dtype=dtype, copy=False)
            else:
                values = np.array(original, dtype="object", copy=False)

    # we copy as need to coerce here
if mask.any():
    values = values.copy()
    values[mask] = cls._internal_fill_value
if inferred_type in ("string", "unicode"):
    # casts from str are always safe since they raise
    # a ValueError if the str cannot be parsed into a float
    values = values.astype(dtype, copy=copy)
else:
    values = dtype_cls._safe_cast(values, dtype, copy=False)

exit((values, mask, dtype, inferred_type))
