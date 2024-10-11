# Extracted from ./data/repos/pandas/pandas/core/reshape/tile.py
"""
    if the passed data is of datetime/timedelta, bool or nullable int type,
    this method converts it to numeric so that cut or qcut method can
    handle it
    """
dtype = None

if is_datetime64tz_dtype(x.dtype):
    dtype = x.dtype
elif is_datetime64_dtype(x.dtype):
    x = to_datetime(x).astype("datetime64[ns]", copy=False)
    dtype = np.dtype("datetime64[ns]")
elif is_timedelta64_dtype(x.dtype):
    x = to_timedelta(x)
    dtype = np.dtype("timedelta64[ns]")
elif is_bool_dtype(x.dtype):
    # GH 20303
    x = x.astype(np.int64)
# To support cut and qcut for IntegerArray we convert to float dtype.
# Will properly support in the future.
# https://github.com/pandas-dev/pandas/pull/31290
# https://github.com/pandas-dev/pandas/issues/31389
elif is_extension_array_dtype(x.dtype) and is_numeric_dtype(x.dtype):
    x = x.to_numpy(dtype=np.float64, na_value=np.nan)

if dtype is not None:
    # GH 19768: force NaT to NaN during integer conversion
    x = np.where(x.notna(), x.view(np.int64), np.nan)

exit((x, dtype))
