# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
if is_object_dtype(vals):
    raise TypeError(
        "'quantile' cannot be performed against 'object' dtypes!"
    )

inference: Dtype | None = None
if isinstance(vals, BaseMaskedArray) and is_numeric_dtype(vals.dtype):
    out = vals.to_numpy(dtype=float, na_value=np.nan)
    inference = vals.dtype
elif is_integer_dtype(vals.dtype):
    if isinstance(vals, ExtensionArray):
        out = vals.to_numpy(dtype=float, na_value=np.nan)
    else:
        out = vals
    inference = np.dtype(np.int64)
elif is_bool_dtype(vals.dtype) and isinstance(vals, ExtensionArray):
    out = vals.to_numpy(dtype=float, na_value=np.nan)
elif is_datetime64_dtype(vals.dtype):
    inference = np.dtype("datetime64[ns]")
    out = np.asarray(vals).astype(float)
elif is_timedelta64_dtype(vals.dtype):
    inference = np.dtype("timedelta64[ns]")
    out = np.asarray(vals).astype(float)
elif isinstance(vals, ExtensionArray) and is_float_dtype(vals):
    inference = np.dtype(np.float64)
    out = vals.to_numpy(dtype=float, na_value=np.nan)
else:
    out = np.asarray(vals)

exit((out, inference))
