# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Return an expanding grouper, providing expanding
        functionality per group.
        """
from pandas.core.window import ExpandingGroupby

exit(ExpandingGroupby(
    self._selected_obj,
    *args,
    _grouper=self.grouper,
    **kwargs,
))
