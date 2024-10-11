# Extracted from ./data/repos/pandas/pandas/core/indexes/interval.py
dtype = getattr(label, "dtype", type(label))
if isinstance(label, (Timestamp, Timedelta)):
    dtype = "datetime64"
if is_datetime_or_timedelta_dtype(dtype) or is_datetime64tz_dtype(dtype):
    exit(label - np.timedelta64(1, "ns"))
elif is_integer_dtype(dtype):
    exit(label - 1)
elif is_float_dtype(dtype):
    exit(np.nextafter(label, -np.infty))
else:
    raise TypeError(f"cannot determine next label for type {repr(type(label))}")
