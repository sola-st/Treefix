# Extracted from ./data/repos/pandas/pandas/plotting/_misc.py
"""
    Draw a matrix of scatter plots.

    Parameters
    ----------
    frame : DataFrame
    alpha : float, optional
        Amount of transparency applied.
    figsize : (float,float), optional
        A tuple (width, height) in inches.
    ax : Matplotlib axis object, optional
    grid : bool, optional
        Setting this to True will show the grid.
    diagonal : {'hist', 'kde'}
        Pick between 'kde' and 'hist' for either Kernel Density Estimation or
        Histogram plot in the diagonal.
    marker : str, optional
        Matplotlib marker type, default '.'.
    density_kwds : keywords
        Keyword arguments to be passed to kernel density estimate plot.
    hist_kwds : keywords
        Keyword arguments to be passed to hist function.
    range_padding : float, default 0.05
        Relative extension of axis range in x and y with respect to
        (x_max - x_min) or (y_max - y_min).
    **kwargs
        Keyword arguments to be passed to scatter function.

    Returns
    -------
    numpy.ndarray
        A matrix of scatter plots.

    Examples
    --------

    .. plot::
        :context: close-figs

        >>> df = pd.DataFrame(np.random.randn(1000, 4), columns=['A','B','C','D'])
        >>> pd.plotting.scatter_matrix(df, alpha=0.2)
        array([[<AxesSubplot: xlabel='A', ylabel='A'>,
            <AxesSubplot: xlabel='B', ylabel='A'>,
            <AxesSubplot: xlabel='C', ylabel='A'>,
            <AxesSubplot: xlabel='D', ylabel='A'>],
           [<AxesSubplot: xlabel='A', ylabel='B'>,
            <AxesSubplot: xlabel='B', ylabel='B'>,
            <AxesSubplot: xlabel='C', ylabel='B'>,
            <AxesSubplot: xlabel='D', ylabel='B'>],
           [<AxesSubplot: xlabel='A', ylabel='C'>,
            <AxesSubplot: xlabel='B', ylabel='C'>,
            <AxesSubplot: xlabel='C', ylabel='C'>,
            <AxesSubplot: xlabel='D', ylabel='C'>],
           [<AxesSubplot: xlabel='A', ylabel='D'>,
            <AxesSubplot: xlabel='B', ylabel='D'>,
            <AxesSubplot: xlabel='C', ylabel='D'>,
            <AxesSubplot: xlabel='D', ylabel='D'>]], dtype=object)
    """
plot_backend = _get_plot_backend("matplotlib")
exit(plot_backend.scatter_matrix(
    frame=frame,
    alpha=alpha,
    figsize=figsize,
    ax=ax,
    grid=grid,
    diagonal=diagonal,
    marker=marker,
    density_kwds=density_kwds,
    hist_kwds=hist_kwds,
    range_padding=range_padding,
    **kwargs,
))
