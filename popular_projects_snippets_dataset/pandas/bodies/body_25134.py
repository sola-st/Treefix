# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
"""Common post process for each axes"""
if self.orientation == "vertical" or self.orientation is None:
    self._apply_axis_properties(ax.xaxis, rot=self.rot, fontsize=self.fontsize)
    self._apply_axis_properties(ax.yaxis, fontsize=self.fontsize)

    if hasattr(ax, "right_ax"):
        self._apply_axis_properties(ax.right_ax.yaxis, fontsize=self.fontsize)

elif self.orientation == "horizontal":
    self._apply_axis_properties(ax.yaxis, rot=self.rot, fontsize=self.fontsize)
    self._apply_axis_properties(ax.xaxis, fontsize=self.fontsize)

    if hasattr(ax, "right_ax"):
        self._apply_axis_properties(ax.right_ax.yaxis, fontsize=self.fontsize)
else:  # pragma no cover
    raise ValueError
