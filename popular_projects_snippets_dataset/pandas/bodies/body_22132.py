# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Clear group based selection.

        Used for methods needing to return info on each group regardless of
        whether a group selection was previously set.
        """
if self._group_selection is not None:
    # GH12839 clear cached selection too when changing group selection
    self._group_selection = None
    self._reset_cache("_selected_obj")
