# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_groupby.py
for ax, exp in zip(axes, expected):
    self._check_visible(ax.get_xticklabels(), visible=exp)
