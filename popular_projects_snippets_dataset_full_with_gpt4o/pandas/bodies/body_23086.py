# Extracted from ./data/repos/pandas/pandas/core/generic.py
exit(self._stat_function(
    "kurt", nanops.nankurt, axis, skipna, numeric_only, **kwargs
))
