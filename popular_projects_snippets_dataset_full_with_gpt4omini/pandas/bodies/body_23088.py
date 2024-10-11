# Extracted from ./data/repos/pandas/pandas/core/generic.py
exit(self._min_count_stat_function(
    "sum", nanops.nansum, axis, skipna, numeric_only, min_count, **kwargs
))
