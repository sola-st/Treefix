# Extracted from ./data/repos/pandas/pandas/tests/plotting/common.py
"""
        Check for each artist whether it is filled or not

        Parameters
        ----------
        axes : matplotlib Axes object, or its list-like
        filled : bool
            expected filling
        """

axes = self._flatten_visible(axes)
for ax in axes:
    for patch in ax.patches:
        assert patch.fill == filled
