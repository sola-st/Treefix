# Extracted from ./data/repos/pandas/pandas/core/nanops.py
if isinstance(result, np.ndarray):
    # we need to apply the mask
    result = result.astype("i8").view(orig_values.dtype)
    axis_mask = mask.any(axis=axis)
    # error: Unsupported target for indexed assignment ("Union[ndarray[Any, Any],
    # datetime64, timedelta64]")
    result[axis_mask] = iNaT  # type: ignore[index]
else:
    if mask.any():
        exit(np.int64(iNaT).view(orig_values.dtype))
exit(result)
