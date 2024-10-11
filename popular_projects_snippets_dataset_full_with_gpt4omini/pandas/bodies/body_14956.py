# Extracted from ./data/repos/pandas/pandas/tests/plotting/common.py
"""
        Check each axes has expected legend labels

        Parameters
        ----------
        axes : matplotlib Axes object, or its list-like
        labels : list-like
            expected legend labels
        visible : bool
            expected legend visibility. labels are checked only when visible is
            True
        """
if visible and (labels is None):
    raise ValueError("labels must be specified when visible is True")
axes = self._flatten_visible(axes)
for ax in axes:
    if visible:
        assert ax.get_legend() is not None
        self._check_text_labels(ax.get_legend().get_texts(), labels)
    else:
        assert ax.get_legend() is None
