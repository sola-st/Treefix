# Extracted from ./data/repos/pandas/pandas/core/generic.py
exit(self._logical_func(
    "all", nanops.nanall, axis, bool_only, skipna, **kwargs
))
