# Extracted from ./data/repos/pandas/pandas/plotting/_misc.py
"""
    Autocorrelation plot for time series.

    Parameters
    ----------
    series : Series
        The time series to visualize.
    ax : Matplotlib axis object, optional
        The matplotlib axis object to use.
    **kwargs
        Options to pass to matplotlib plotting method.

    Returns
    -------
    matplotlib.axis.Axes

    Examples
    --------
    The horizontal lines in the plot correspond to 95% and 99% confidence bands.

    The dashed line is 99% confidence band.

    .. plot::
        :context: close-figs

        >>> spacing = np.linspace(-9 * np.pi, 9 * np.pi, num=1000)
        >>> s = pd.Series(0.7 * np.random.rand(1000) + 0.3 * np.sin(spacing))
        >>> pd.plotting.autocorrelation_plot(s)
        <AxesSubplot: title={'center': 'width'}, xlabel='Lag', ylabel='Autocorrelation'>
    """
plot_backend = _get_plot_backend("matplotlib")
exit(plot_backend.autocorrelation_plot(series=series, ax=ax, **kwargs))
