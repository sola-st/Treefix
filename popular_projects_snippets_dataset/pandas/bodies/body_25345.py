# Extracted from ./data/repos/pandas/pandas/plotting/_misc.py
"""
    Generate a matplotlib plot for visualising clusters of multivariate data.

    Andrews curves have the functional form:

    f(t) = x_1/sqrt(2) + x_2 sin(t) + x_3 cos(t) +
           x_4 sin(2t) + x_5 cos(2t) + ...

    Where x coefficients correspond to the values of each dimension and t is
    linearly spaced between -pi and +pi. Each row of frame then corresponds to
    a single curve.

    Parameters
    ----------
    frame : DataFrame
        Data to be plotted, preferably normalized to (0.0, 1.0).
    class_column : label
        Name of the column containing class names.
    ax : axes object, default None
        Axes to use.
    samples : int
        Number of points to plot in each curve.
    color : str, list[str] or tuple[str], optional
        Colors to use for the different classes. Colors can be strings
        or 3-element floating point RGB values.
    colormap : str or matplotlib colormap object, default None
        Colormap to select colors from. If a string, load colormap with that
        name from matplotlib.
    **kwargs
        Options to pass to matplotlib plotting method.

    Returns
    -------
    class:`matplotlip.axis.Axes`

    Examples
    --------

    .. plot::
        :context: close-figs

        >>> df = pd.read_csv(
        ...     'https://raw.githubusercontent.com/pandas-dev/'
        ...     'pandas/main/pandas/tests/io/data/csv/iris.csv'
        ... )
        >>> pd.plotting.andrews_curves(df, 'Name')
        <AxesSubplot: title={'center': 'width'}>
    """
plot_backend = _get_plot_backend("matplotlib")
exit(plot_backend.andrews_curves(
    frame=frame,
    class_column=class_column,
    ax=ax,
    samples=samples,
    color=color,
    colormap=colormap,
    **kwargs,
))
