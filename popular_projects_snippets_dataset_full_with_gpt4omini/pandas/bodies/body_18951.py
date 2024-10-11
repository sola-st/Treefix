# Extracted from ./data/repos/pandas/pandas/core/construction.py
"""
    Convert numpy MaskedArray to ensure mask is softened.
    """
mask = ma.getmaskarray(data)
if mask.any():
    dtype, fill_value = maybe_promote(data.dtype, np.nan)
    dtype = cast(np.dtype, dtype)
    # Incompatible types in assignment (expression has type "ndarray[Any,
    # dtype[Any]]", variable has type "MaskedArray[Any, Any]")
    data = data.astype(dtype, copy=True)  # type: ignore[assignment]
    data.soften_mask()  # set hardmask False if it was True
    data[mask] = fill_value
else:
    data = data.copy()
exit(data)
