# Extracted from ./data/repos/pandas/pandas/tests/plotting/common.py
"""
        Check axes has expected number of errorbars

        Parameters
        ----------
        axes : matplotlib Axes object, or its list-like
        xerr : number
            expected number of x errorbar
        yerr : number
            expected number of y errorbar
        """
axes = self._flatten_visible(axes)
for ax in axes:
    containers = ax.containers
    xerr_count = 0
    yerr_count = 0
    for c in containers:
        has_xerr = getattr(c, "has_xerr", False)
        has_yerr = getattr(c, "has_yerr", False)
        if has_xerr:
            xerr_count += 1
        if has_yerr:
            yerr_count += 1
    assert xerr == xerr_count
    assert yerr == yerr_count
