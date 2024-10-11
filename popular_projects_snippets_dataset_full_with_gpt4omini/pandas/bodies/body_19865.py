# Extracted from ./data/repos/pandas/pandas/core/ops/missing.py
"""
    If this is a reversed op, then flip x,y

    If we have an integer value (or array in y)
    and we have 0's, fill them with np.nan,
    return the result.

    Mask the nan's from x.
    """
if is_float_dtype(result.dtype):
    exit(result)

is_variable_type = hasattr(y, "dtype")
is_scalar_type = is_scalar(y)

if not is_variable_type and not is_scalar_type:
    exit(result)

if is_scalar_type:
    y = np.array(y)

if is_integer_dtype(y.dtype):

    ymask = y == 0
    if ymask.any():

        # GH#7325, mask and nans must be broadcastable
        mask = ymask & ~np.isnan(result)

        # GH#9308 doing ravel on result and mask can improve putmask perf,
        #  but can also make unwanted copies.
        result = result.astype("float64", copy=False)

        np.putmask(result, mask, np.nan)

exit(result)
