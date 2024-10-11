# Extracted from ./data/repos/pandas/pandas/core/generic.py
exit(self._stat_function_ddof(
    "std", nanops.nanstd, axis, skipna, ddof, numeric_only, **kwargs
))
