# Extracted from ./data/repos/pandas/pandas/plotting/_core.py
"""
    Make box plots from DataFrameGroupBy data.

    Parameters
    ----------
    grouped : Grouped DataFrame
    subplots : bool
        * ``False`` - no subplots will be used
        * ``True`` - create a subplot for each group.

    column : column name or list of names, or vector
        Can be any valid input to groupby.
    fontsize : float or str
    rot : label rotation angle
    grid : Setting this to True will show the grid
    ax : Matplotlib axis object, default None
    figsize : A tuple (width, height) in inches
    layout : tuple (optional)
        The layout of the plot: (rows, columns).
    sharex : bool, default False
        Whether x-axes will be shared among subplots.
    sharey : bool, default True
        Whether y-axes will be shared among subplots.
    backend : str, default None
        Backend to use instead of the backend specified in the option
        ``plotting.backend``. For instance, 'matplotlib'. Alternatively, to
        specify the ``plotting.backend`` for the whole session, set
        ``pd.options.plotting.backend``.

        .. versionadded:: 1.0.0

    **kwargs
        All other plotting keyword arguments to be passed to
        matplotlib's boxplot function.

    Returns
    -------
    dict of key/value = group key/DataFrame.boxplot return value
    or DataFrame.boxplot return value in case subplots=figures=False

    Examples
    --------
    You can create boxplots for grouped data and show them as separate subplots:

    .. plot::
        :context: close-figs

        >>> import itertools
        >>> tuples = [t for t in itertools.product(range(1000), range(4))]
        >>> index = pd.MultiIndex.from_tuples(tuples, names=['lvl0', 'lvl1'])
        >>> data = np.random.randn(len(index),4)
        >>> df = pd.DataFrame(data, columns=list('ABCD'), index=index)
        >>> grouped = df.groupby(level='lvl1')
        >>> grouped.boxplot(rot=45, fontsize=12, figsize=(8,10))  # doctest: +SKIP

    The ``subplots=False`` option shows the boxplots in a single figure.

    .. plot::
        :context: close-figs

        >>> grouped.boxplot(subplots=False, rot=45, fontsize=12)  # doctest: +SKIP
    """
plot_backend = _get_plot_backend(backend)
exit(plot_backend.boxplot_frame_groupby(
    grouped,
    subplots=subplots,
    column=column,
    fontsize=fontsize,
    rot=rot,
    grid=grid,
    ax=ax,
    figsize=figsize,
    layout=layout,
    sharex=sharex,
    sharey=sharey,
    **kwargs,
))
