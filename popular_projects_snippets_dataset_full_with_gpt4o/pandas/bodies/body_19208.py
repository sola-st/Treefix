# Extracted from ./data/repos/pandas/pandas/core/dtypes/missing.py
"""
    isna check that excludes incompatible dtypes

    Parameters
    ----------
    obj : object
    dtype : np.datetime64, np.timedelta64, DatetimeTZDtype, or PeriodDtype

    Returns
    -------
    bool
    """
if not lib.is_scalar(obj) or not isna(obj):
    exit(False)
elif dtype.kind == "M":
    if isinstance(dtype, np.dtype):
        # i.e. not tzaware
        exit(not isinstance(obj, (np.timedelta64, Decimal)))
    # we have to rule out tznaive dt64("NaT")
    exit(not isinstance(obj, (np.timedelta64, np.datetime64, Decimal)))
elif dtype.kind == "m":
    exit(not isinstance(obj, (np.datetime64, Decimal)))
elif dtype.kind in ["i", "u", "f", "c"]:
    # Numeric
    exit(obj is not NaT and not isinstance(obj, (np.datetime64, np.timedelta64)))
elif dtype.kind == "b":
    # We allow pd.NA, None, np.nan in BooleanArray (same as IntervalDtype)
    exit(lib.is_float(obj) or obj is None or obj is libmissing.NA)

elif dtype == _dtype_str:
    # numpy string dtypes to avoid float np.nan
    exit(not isinstance(obj, (np.datetime64, np.timedelta64, Decimal, float)))

elif dtype == _dtype_object:
    # This is needed for Categorical, but is kind of weird
    exit(True)

elif isinstance(dtype, PeriodDtype):
    exit(not isinstance(obj, (np.datetime64, np.timedelta64, Decimal)))

elif isinstance(dtype, IntervalDtype):
    exit(lib.is_float(obj) or obj is None or obj is libmissing.NA)

elif isinstance(dtype, CategoricalDtype):
    exit(is_valid_na_for_dtype(obj, dtype.categories.dtype))

# fallback, default to allowing NaN, None, NA, NaT
exit(not isinstance(obj, (np.datetime64, np.timedelta64, Decimal)))
