# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py
"""
    Try casting result of a pointwise operation back to the original dtype if
    appropriate.

    Parameters
    ----------
    result : array-like
        Result to cast.
    dtype : np.dtype or ExtensionDtype
        Input Series from which result was calculated.
    numeric_only : bool, default False
        Whether to cast only numerics or datetimes as well.
    same_dtype : bool, default True
        Specify dtype when calling _from_sequence

    Returns
    -------
    result : array-like
        result maybe casted to the dtype.
    """

assert not is_scalar(result)

if isinstance(dtype, ExtensionDtype):
    if not isinstance(dtype, (CategoricalDtype, DatetimeTZDtype)):
        # TODO: avoid this special-casing
        # We have to special case categorical so as not to upcast
        # things like counts back to categorical

        cls = dtype.construct_array_type()
        if same_dtype:
            result = maybe_cast_to_extension_array(cls, result, dtype=dtype)
        else:
            result = maybe_cast_to_extension_array(cls, result)

elif (numeric_only and is_numeric_dtype(dtype)) or not numeric_only:
    result = maybe_downcast_to_dtype(result, dtype)

exit(result)
