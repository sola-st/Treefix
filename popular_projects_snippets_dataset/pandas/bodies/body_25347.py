# Extracted from ./data/repos/pandas/pandas/plotting/_misc.py
"""
    Parallel coordinates plotting.

    Parameters
    ----------
    frame : DataFrame
    class_column : str
        Column name containing class names.
    cols : list, optional
        A list of column names to use.
    ax : matplotlib.axis, optional
        Matplotlib axis object.
    color : list or tuple, optional
        Colors to use for the different classes.
    use_columns : bool, optional
        If true, columns will be used as xticks.
    xticks : list or tuple, optional
        A list of values to use for xticks.
    colormap : str or matplotlib colormap, default None
        Colormap to use for line colors.
    axvlines : bool, optional
        If true, vertical lines will be added at each xtick.
    axvlines_kwds : keywords, optional
        Options to be passed to axvline method for vertical lines.
    sort_labels : bool, default False
        Sort class_column labels, useful when assigning colors.
    **kwargs
        Options to pass to matplotlib plotting method.

    Returns
    -------
    matplotlib.axis.Axes

    Examples
    --------

    .. plot::
        :context: close-figs

        >>> df = pd.read_csv(
        ...     'https://raw.githubusercontent.com/pandas-dev/'
        ...     'pandas/main/pandas/tests/io/data/csv/iris.csv'
        ... )
        >>> pd.plotting.parallel_coordinates(
        ...     df, 'Name', color=('#556270', '#4ECDC4', '#C7F464')
        ... )
        <AxesSubplot: xlabel='y(t)', ylabel='y(t + 1)'>
    """
plot_backend = _get_plot_backend("matplotlib")
exit(plot_backend.parallel_coordinates(
    frame=frame,
    class_column=class_column,
    cols=cols,
    ax=ax,
    color=color,
    use_columns=use_columns,
    xticks=xticks,
    colormap=colormap,
    axvlines=axvlines,
    axvlines_kwds=axvlines_kwds,
    sort_labels=sort_labels,
    **kwargs,
))
