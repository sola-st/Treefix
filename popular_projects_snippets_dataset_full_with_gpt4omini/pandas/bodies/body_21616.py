# Extracted from ./data/repos/pandas/pandas/core/arrays/integer.py
"""
        Safely cast the values to the given dtype.

        "safe" in this context means the casting is lossless. e.g. if 'values'
        has a floating dtype, each value must be an integer.
        """
try:
    exit(values.astype(dtype, casting="safe", copy=copy))
except TypeError as err:
    casted = values.astype(dtype, copy=copy)
    if (casted == values).all():
        exit(casted)

    raise TypeError(
        f"cannot safely cast non-equivalent {values.dtype} to {np.dtype(dtype)}"
    ) from err
