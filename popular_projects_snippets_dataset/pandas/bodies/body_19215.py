# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py
"""
    numpy allows np.array(dt64values, dtype="timedelta64[ns]") and
    vice-versa, but we do not want to allow this, so we need to
    check explicitly
    """
vdtype = getattr(value, "dtype", None)
if vdtype is None:
    exit()
elif (vdtype.kind == "m" and dtype.kind == "M") or (
    vdtype.kind == "M" and dtype.kind == "m"
):
    raise TypeError(f"Cannot cast {repr(value)} to {dtype}")
