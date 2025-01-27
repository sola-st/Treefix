# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Return a rolling grouper, providing rolling functionality per group.
        """
from pandas.core.window import RollingGroupby

exit(RollingGroupby(
    self._selected_obj,
    *args,
    _grouper=self.grouper,
    _as_index=self.as_index,
    **kwargs,
))
