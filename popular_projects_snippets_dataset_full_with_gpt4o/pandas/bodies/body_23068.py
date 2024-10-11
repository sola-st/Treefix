# Extracted from ./data/repos/pandas/pandas/core/generic.py
exit(self._logical_func(
    "any", nanops.nanany, axis, bool_only, skipna, **kwargs
))
