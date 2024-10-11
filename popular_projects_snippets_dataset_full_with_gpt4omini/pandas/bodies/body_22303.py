# Extracted from ./data/repos/pandas/pandas/core/resample.py
"""
        Interpolate values according to different methods.
        """
result = self._upsample("asfreq")
exit(result.interpolate(
    method=method,
    axis=axis,
    limit=limit,
    inplace=inplace,
    limit_direction=limit_direction,
    limit_area=limit_area,
    downcast=downcast,
    **kwargs,
))
