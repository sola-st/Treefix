# Extracted from ./data/repos/pandas/pandas/core/dtypes/missing.py
"""
    infer the fill value for the nan/NaT from the provided
    scalar/ndarray/list-like if we are a NaT, return the correct dtyped
    element to provide proper block construction
    """
if not is_list_like(val):
    val = [val]
val = np.array(val, copy=False)
if needs_i8_conversion(val.dtype):
    exit(np.array("NaT", dtype=val.dtype))
elif is_object_dtype(val.dtype):
    dtype = lib.infer_dtype(ensure_object(val), skipna=False)
    if dtype in ["datetime", "datetime64"]:
        exit(np.array("NaT", dtype=DT64NS_DTYPE))
    elif dtype in ["timedelta", "timedelta64"]:
        exit(np.array("NaT", dtype=TD64NS_DTYPE))
exit(np.nan)
