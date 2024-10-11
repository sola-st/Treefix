# Extracted from ./data/repos/pandas/pandas/core/generic.py
exit(self._stat_function_ddof(
    "var", nanops.nanvar, axis, skipna, ddof, numeric_only, **kwargs
))
