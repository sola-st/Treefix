# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/plotting/_core.py
from l3.Runtime import _l_
"""
    Draw histogram of the input series using matplotlib.

    Parameters
    ----------
    by : object, optional
        If passed, then used to form histograms for separate groups.
    ax : matplotlib axis object
        If not passed, uses gca().
    grid : bool, default True
        Whether to show axis grid lines.
    xlabelsize : int, default None
        If specified changes the x-axis label size.
    xrot : float, default None
        Rotation of x axis labels.
    ylabelsize : int, default None
        If specified changes the y-axis label size.
    yrot : float, default None
        Rotation of y axis labels.
    figsize : tuple, default None
        Figure size in inches by default.
    bins : int or sequence, default 10
        Number of histogram bins to be used. If an integer is given, bins + 1
        bin edges are calculated and returned. If bins is a sequence, gives
        bin edges, including left edge of first bin and right edge of last
        bin. In this case, bins is returned unmodified.
    backend : str, default None
        Backend to use instead of the backend specified in the option
        ``plotting.backend``. For instance, 'matplotlib'. Alternatively, to
        specify the ``plotting.backend`` for the whole session, set
        ``pd.options.plotting.backend``.

        .. versionadded:: 1.0.0

    legend : bool, default False
        Whether to show the legend.

        .. versionadded:: 1.1.0

    **kwargs
        To be passed to the actual plotting function.

    Returns
    -------
    matplotlib.AxesSubplot
        A histogram plot.

    See Also
    --------
    matplotlib.axes.Axes.hist : Plot a histogram using matplotlib.
    """
plot_backend = _get_plot_backend(backend)
_l_(20268)
aux = plot_backend.hist_series(
    self,
    by=by,
    ax=ax,
    grid=grid,
    xlabelsize=xlabelsize,
    xrot=xrot,
    ylabelsize=ylabelsize,
    yrot=yrot,
    figsize=figsize,
    bins=bins,
    legend=legend,
    **kwargs,
)
_l_(20269)
exit(aux)
