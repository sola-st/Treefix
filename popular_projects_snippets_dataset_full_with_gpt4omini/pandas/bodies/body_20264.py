# Extracted from ./data/repos/pandas/pandas/core/missing.py
"""
    Perform an actual interpolation of values, values will be make 2-d if
    needed fills inplace, returns the result.

    Parameters
    ----------
    values: np.ndarray
        Input array.
    method: str, default "pad"
        Interpolation method. Could be "bfill" or "pad"
    axis: 0 or 1
        Interpolation axis
    limit: int, optional
        Index limit on interpolation.
    limit_area: str, optional
        Limit area for interpolation. Can be "inside" or "outside"

    Notes
    -----
    Modifies values in-place.
    """
if limit_area is not None:
    np.apply_along_axis(
        # error: Argument 1 to "apply_along_axis" has incompatible type
        # "partial[None]"; expected
        # "Callable[..., Union[_SupportsArray[dtype[<nothing>]],
        # Sequence[_SupportsArray[dtype[<nothing>]]],
        # Sequence[Sequence[_SupportsArray[dtype[<nothing>]]]],
        # Sequence[Sequence[Sequence[_SupportsArray[dtype[<nothing>]]]]],
        # Sequence[Sequence[Sequence[Sequence[_
        # SupportsArray[dtype[<nothing>]]]]]]]]"
        partial(  # type: ignore[arg-type]
            _interpolate_with_limit_area,
            method=method,
            limit=limit,
            limit_area=limit_area,
        ),
        # error: Argument 2 to "apply_along_axis" has incompatible type
        # "Union[str, int]"; expected "SupportsIndex"
        axis,  # type: ignore[arg-type]
        values,
    )
    exit()

transf = (lambda x: x) if axis == 0 else (lambda x: x.T)

# reshape a 1 dim if needed
if values.ndim == 1:
    if axis != 0:  # pragma: no cover
        raise AssertionError("cannot interpolate on a ndim == 1 with axis != 0")
    values = values.reshape(tuple((1,) + values.shape))

method = clean_fill_method(method)
tvalues = transf(values)

# _pad_2d and _backfill_2d both modify tvalues inplace
if method == "pad":
    _pad_2d(tvalues, limit=limit)
else:
    _backfill_2d(tvalues, limit=limit)

exit()
