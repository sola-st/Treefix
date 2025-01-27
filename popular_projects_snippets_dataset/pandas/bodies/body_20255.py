# Extracted from ./data/repos/pandas/pandas/core/missing.py
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
