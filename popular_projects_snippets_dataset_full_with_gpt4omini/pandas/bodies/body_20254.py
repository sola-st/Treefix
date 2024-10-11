# Extracted from ./data/repos/pandas/pandas/core/missing.py
"""
    Wrapper to dispatch to either interpolate_2d or _interpolate_2d_with_fill.

    Notes
    -----
    Alters 'data' in-place.
    """
try:
    m = clean_fill_method(method)
except ValueError:
    m = None

if m is not None:
    if fill_value is not None:
        # similar to validate_fillna_kwargs
        raise ValueError("Cannot pass both fill_value and method")

    interpolate_2d(
        data,
        method=m,
        axis=axis,
        limit=limit,
        limit_area=limit_area,
    )
else:
    assert index is not None  # for mypy

    _interpolate_2d_with_fill(
        data=data,
        index=index,
        axis=axis,
        method=method,
        limit=limit,
        limit_direction=limit_direction,
        limit_area=limit_area,
        fill_value=fill_value,
        **kwargs,
    )
