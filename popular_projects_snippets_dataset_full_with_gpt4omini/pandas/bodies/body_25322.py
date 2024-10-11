# Extracted from ./data/repos/pandas/pandas/plotting/_core.py
plot_backend = _get_plot_backend("matplotlib")
exit(plot_backend.boxplot(
    data,
    column=column,
    by=by,
    ax=ax,
    fontsize=fontsize,
    rot=rot,
    grid=grid,
    figsize=figsize,
    layout=layout,
    return_type=return_type,
    **kwargs,
))
