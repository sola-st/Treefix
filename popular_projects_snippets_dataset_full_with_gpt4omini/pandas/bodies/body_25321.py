# Extracted from ./data/repos/pandas/pandas/plotting/_core.py
"""
    Make a histogram of the DataFrame's columns.

    A `histogram`_ is a representation of the distribution of data.
    This function calls :meth:`matplotlib.pyplot.hist`, on each series in
    the DataFrame, resulting in one histogram per column.

    .. _histogram: https://en.wikipedia.org/wiki/Histogram

    Parameters
    ----------
    data : DataFrame
        The pandas object holding the data.
    column : str or sequence, optional
        If passed, will be used to limit data to a subset of columns.
    by : object, optional
        If passed, then used to form histograms for separate groups.
    grid : bool, default True
        Whether to show axis grid lines.
    xlabelsize : int, default None
        If specified changes the x-axis label size.
    xrot : float, default None
        Rotation of x axis labels. For example, a value of 90 displays the
        x labels rotated 90 degrees clockwise.
    ylabelsize : int, default None
        If specified changes the y-axis label size.
    yrot : float, default None
        Rotation of y axis labels. For example, a value of 90 displays the
        y labels rotated 90 degrees clockwise.
    ax : Matplotlib axes object, default None
        The axes to plot the histogram on.
    sharex : bool, default True if ax is None else False
        In case subplots=True, share x axis and set some x axis labels to
        invisible; defaults to True if ax is None otherwise False if an ax
        is passed in.
        Note that passing in both an ax and sharex=True will alter all x axis
        labels for all subplots in a figure.
    sharey : bool, default False
        In case subplots=True, share y axis and set some y axis labels to
        invisible.
    figsize : tuple, optional
        The size in inches of the figure to create. Uses the value in
        `matplotlib.rcParams` by default.
    layout : tuple, optional
        Tuple of (rows, columns) for the layout of the histograms.
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
        All other plotting keyword arguments to be passed to
        :meth:`matplotlib.pyplot.hist`.

    Returns
    -------
    matplotlib.AxesSubplot or numpy.ndarray of them

    See Also
    --------
    matplotlib.pyplot.hist : Plot a histogram using matplotlib.

    Examples
    --------
    This example draws a histogram based on the length and width of
    some animals, displayed in three bins

    .. plot::
        :context: close-figs

        >>> df = pd.DataFrame({
        ...     'length': [1.5, 0.5, 1.2, 0.9, 3],
        ...     'width': [0.7, 0.2, 0.15, 0.2, 1.1]
        ...     }, index=['pig', 'rabbit', 'duck', 'chicken', 'horse'])
        >>> hist = df.hist(bins=3)
    """
plot_backend = _get_plot_backend(backend)
exit(plot_backend.hist_frame(
    data,
    column=column,
    by=by,
    grid=grid,
    xlabelsize=xlabelsize,
    xrot=xrot,
    ylabelsize=ylabelsize,
    yrot=yrot,
    ax=ax,
    sharex=sharex,
    sharey=sharey,
    figsize=figsize,
    layout=layout,
    legend=legend,
    bins=bins,
    **kwargs,
))
