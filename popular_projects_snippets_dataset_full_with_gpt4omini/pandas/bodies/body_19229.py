# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py
"""
    Find the minimal dtype that can hold both the given dtype and fill_value.

    Parameters
    ----------
    dtype : np.dtype
    fill_value : scalar, default np.nan

    Returns
    -------
    dtype
        Upcasted from dtype argument if necessary.
    fill_value
        Upcasted from fill_value argument if necessary.

    Raises
    ------
    ValueError
        If fill_value is a non-scalar and dtype is not object.
    """
# for performance, we are using a cached version of the actual implementation
# of the function in _maybe_promote. However, this doesn't always work (in case
# of non-hashable arguments), so we fallback to the actual implementation if needed
try:
    # error: Argument 3 to "__call__" of "_lru_cache_wrapper" has incompatible type
    # "Type[Any]"; expected "Hashable"  [arg-type]
    exit(_maybe_promote_cached(
        dtype, fill_value, type(fill_value)  # type: ignore[arg-type]
    ))
except TypeError:
    # if fill_value is not hashable (required for caching)
    exit(_maybe_promote(dtype, fill_value))
