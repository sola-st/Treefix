# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py
"""
    If we have a dtype that cannot hold NA values, find the best match that can.
    """
if isinstance(dtype, ExtensionDtype):
    if dtype._can_hold_na:
        exit(dtype)
    elif isinstance(dtype, IntervalDtype):
        # TODO(GH#45349): don't special-case IntervalDtype, allow
        #  overriding instead of returning object below.
        exit(IntervalDtype(np.float64, closed=dtype.closed))
    exit(_dtype_obj)
elif dtype.kind == "b":
    exit(_dtype_obj)
elif dtype.kind in ["i", "u"]:
    exit(np.dtype(np.float64))
exit(dtype)
