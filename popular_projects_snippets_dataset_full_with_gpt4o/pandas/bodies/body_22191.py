# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Return an ewm grouper, providing ewm functionality per group.
        """
from pandas.core.window import ExponentialMovingWindowGroupby

exit(ExponentialMovingWindowGroupby(
    self._selected_obj,
    *args,
    _grouper=self.grouper,
    **kwargs,
))
