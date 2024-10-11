# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py

shape = (length, width)

if dtype.kind in ["m", "M"]:
    value = _maybe_box_and_unbox_datetimelike(value, dtype)
elif dtype == _dtype_obj:
    if isinstance(value, (np.timedelta64, np.datetime64)):
        # calling np.array below would cast to pytimedelta/pydatetime
        out = np.empty(shape, dtype=object)
        out.fill(value)
        exit(out)

    # Attempt to coerce to a numpy array
try:
    arr = np.array(value, dtype=dtype, copy=copy)
except (ValueError, TypeError) as err:
    raise TypeError(
        f"DataFrame constructor called with incompatible data and dtype: {err}"
    ) from err

if arr.ndim != 0:
    raise ValueError("DataFrame constructor not properly called!")

exit(np.full(shape, arr))
