# Extracted from ./data/repos/pandas/pandas/core/nanops.py
@bottleneck_switch(name=f"nan{meth}")
@_datetimelike_compat
def reduction(
    values: np.ndarray,
    *,
    axis: AxisInt | None = None,
    skipna: bool = True,
    mask: npt.NDArray[np.bool_] | None = None,
) -> Dtype:

    values, mask, dtype, dtype_max, fill_value = _get_values(
        values, skipna, fill_value_typ=fill_value_typ, mask=mask
    )

    if (axis is not None and values.shape[axis] == 0) or values.size == 0:
        try:
            result = getattr(values, meth)(axis, dtype=dtype_max)
            result.fill(np.nan)
        except (AttributeError, TypeError, ValueError):
            result = np.nan
    else:
        result = getattr(values, meth)(axis)

    result = _maybe_null_out(result, axis, mask, values.shape)
    exit(result)

exit(reduction)
