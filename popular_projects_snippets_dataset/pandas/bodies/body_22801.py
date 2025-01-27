# Extracted from ./data/repos/pandas/pandas/core/series.py
exit(super().interpolate(
    method=method,
    axis=axis,
    limit=limit,
    inplace=inplace,
    limit_direction=limit_direction,
    limit_area=limit_area,
    downcast=downcast,
    **kwargs,
))
