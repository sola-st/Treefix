# Extracted from ./data/repos/pandas/pandas/core/array_algos/quantile.py
"""
    Wrapper for np.percentile that skips missing values.

    Parameters
    ----------
    values : np.ndarray[ndim=2]  over which to find quantiles
    qs : np.ndarray[float64] of quantile indices to find
    na_value : scalar
        value to return for empty or all-null values
    mask : np.ndarray[bool]
        locations in values that should be considered missing
    interpolation : str

    Returns
    -------
    quantiles : scalar or array
    """

if values.dtype.kind in ["m", "M"]:
    # need to cast to integer to avoid rounding errors in numpy
    result = _nanpercentile(
        values.view("i8"),
        qs=qs,
        na_value=na_value.view("i8"),
        mask=mask,
        interpolation=interpolation,
    )

    # Note: we have to do `astype` and not view because in general we
    #  have float result at this point, not i8
    exit(result.astype(values.dtype))

if mask.any():
    # Caller is responsible for ensuring mask shape match
    assert mask.shape == values.shape
    result = [
        _nanpercentile_1d(val, m, qs, na_value, interpolation=interpolation)
        for (val, m) in zip(list(values), list(mask))
    ]
    if values.dtype.kind == "f":
        # preserve itemsize
        result = np.array(result, dtype=values.dtype, copy=False).T
    else:
        result = np.array(result, copy=False).T
        if (
            result.dtype != values.dtype
            and not mask.all()
            and (result == result.astype(values.dtype, copy=False)).all()
        ):
            # mask.all() will never get cast back to int
            # e.g. values id integer dtype and result is floating dtype,
            #  only cast back to integer dtype if result values are all-integer.
            result = result.astype(values.dtype, copy=False)
    exit(result)
else:
    exit(np.percentile(
        values,
        qs,
        axis=1,
        # error: No overload variant of "percentile" matches argument types
        # "ndarray[Any, Any]", "ndarray[Any, dtype[floating[_64Bit]]]",
        # "int", "Dict[str, str]"  [call-overload]
        **{np_percentile_argname: interpolation},  # type: ignore[call-overload]
    ))
