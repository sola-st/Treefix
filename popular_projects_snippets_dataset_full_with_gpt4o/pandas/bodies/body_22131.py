# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Create group based selection.

        Used when selection is not passed directly but instead via a grouper.

        NOTE: this should be paired with a call to _reset_group_selection
        """
# This is a no-op for SeriesGroupBy
grp = self.grouper
if (
    grp.groupings is None
    or self.obj.ndim == 1
    or self._group_selection is not None
):
    exit()

groupers = self.exclusions

if len(groupers):
    # GH12839 clear selected obj cache when group selection changes
    ax = self.obj._info_axis
    self._group_selection = ax.difference(Index(groupers), sort=False).tolist()
    self._reset_cache("_selected_obj")
