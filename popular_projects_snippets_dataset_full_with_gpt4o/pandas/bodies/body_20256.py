# Extracted from ./data/repos/pandas/pandas/core/missing.py
"""
    Column-wise application of _interpolate_1d.

    Notes
    -----
    Alters 'data' in-place.

    The signature does differ from _interpolate_1d because it only
    includes what is needed for Block.interpolate.
    """
# validate the interp method
clean_interp_method(method, index, **kwargs)

if is_valid_na_for_dtype(fill_value, data.dtype):
    fill_value = na_value_for_dtype(data.dtype, compat=False)

if method == "time":
    if not needs_i8_conversion(index.dtype):
        raise ValueError(
            "time-weighted interpolation only works "
            "on Series or DataFrames with a "
            "DatetimeIndex"
        )
    method = "values"

valid_limit_directions = ["forward", "backward", "both"]
limit_direction = limit_direction.lower()
if limit_direction not in valid_limit_directions:
    raise ValueError(
        "Invalid limit_direction: expecting one of "
        f"{valid_limit_directions}, got '{limit_direction}'."
    )

if limit_area is not None:
    valid_limit_areas = ["inside", "outside"]
    limit_area = limit_area.lower()
    if limit_area not in valid_limit_areas:
        raise ValueError(
            f"Invalid limit_area: expecting one of {valid_limit_areas}, got "
            f"{limit_area}."
        )

    # default limit is unlimited GH #16282
limit = algos.validate_limit(nobs=None, limit=limit)

indices = _index_to_interp_indices(index, method)

def func(yvalues: np.ndarray) -> None:
    # process 1-d slices in the axis direction

    _interpolate_1d(
        indices=indices,
        yvalues=yvalues,
        method=method,
        limit=limit,
        limit_direction=limit_direction,
        limit_area=limit_area,
        fill_value=fill_value,
        bounds_error=False,
        **kwargs,
    )

# error: Argument 1 to "apply_along_axis" has incompatible type
# "Callable[[ndarray[Any, Any]], None]"; expected "Callable[...,
# Union[_SupportsArray[dtype[<nothing>]], Sequence[_SupportsArray
# [dtype[<nothing>]]], Sequence[Sequence[_SupportsArray[dtype[<nothing>]]]],
# Sequence[Sequence[Sequence[_SupportsArray[dtype[<nothing>]]]]],
# Sequence[Sequence[Sequence[Sequence[_SupportsArray[dtype[<nothing>]]]]]]]]"
np.apply_along_axis(func, axis, data)  # type: ignore[arg-type]
