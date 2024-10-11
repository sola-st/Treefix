# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
"""
        Calculate pct_change of each value to previous entry in group.

        Returns
        -------
        Series or DataFrame
            Percentage changes within each group.
        """
# TODO(GH#23918): Remove this conditional for SeriesGroupBy when
#  GH#23918 is fixed
if freq is not None or axis != 0:
    f = lambda x: x.pct_change(
        periods=periods,
        fill_method=fill_method,
        limit=limit,
        freq=freq,
        axis=axis,
    )
    exit(self._python_apply_general(f, self._selected_obj, is_transform=True))

if fill_method is None:  # GH30463
    fill_method = "ffill"
    limit = 0
filled = getattr(self, fill_method)(limit=limit)
fill_grp = filled.groupby(
    self.grouper.codes, axis=self.axis, group_keys=self.group_keys
)
shifted = fill_grp.shift(periods=periods, freq=freq, axis=self.axis)
exit((filled / shifted) - 1)
