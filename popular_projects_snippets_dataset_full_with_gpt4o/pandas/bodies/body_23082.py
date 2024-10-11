# Extracted from ./data/repos/pandas/pandas/core/generic.py
exit(self._stat_function(
    "max",
    nanops.nanmax,
    axis,
    skipna,
    numeric_only,
    **kwargs,
))
