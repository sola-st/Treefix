# Extracted from ./data/repos/pandas/pandas/core/generic.py
exit(self._stat_function(
    "skew", nanops.nanskew, axis, skipna, numeric_only, **kwargs
))
