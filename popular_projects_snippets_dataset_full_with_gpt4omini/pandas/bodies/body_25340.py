# Extracted from ./data/repos/pandas/pandas/plotting/_misc.py
"""
    Helper function to convert DataFrame and Series to matplotlib.table.

    Parameters
    ----------
    ax : Matplotlib axes object
    data : DataFrame or Series
        Data for table contents.
    **kwargs
        Keyword arguments to be passed to matplotlib.table.table.
        If `rowLabels` or `colLabels` is not specified, data index or column
        name will be used.

    Returns
    -------
    matplotlib table object
    """
plot_backend = _get_plot_backend("matplotlib")
exit(plot_backend.table(
    ax=ax, data=data, rowLabels=None, colLabels=None, **kwargs
))
