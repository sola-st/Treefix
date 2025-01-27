# Extracted from ./data/repos/pandas/pandas/core/generic.py
exit(self._stat_function_ddof(
    "sem", nanops.nansem, axis, skipna, ddof, numeric_only, **kwargs
))
