# Extracted from ./data/repos/pandas/pandas/core/generic.py
exit(self._stat_function(
    "median", nanops.nanmedian, axis, skipna, numeric_only, **kwargs
))
