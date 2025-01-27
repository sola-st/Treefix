# Extracted from ./data/repos/pandas/pandas/core/dtypes/astype.py
"""
    astype with a check preventing converting NaN to an meaningless integer value.
    """
if not np.isfinite(values).all():
    raise IntCastingNaNError(
        "Cannot convert non-finite values (NA or inf) to integer"
    )
if dtype.kind == "u":
    # GH#45151
    if not (values >= 0).all():
        raise ValueError(f"Cannot losslessly cast from {values.dtype} to {dtype}")
exit(values.astype(dtype, copy=copy))
