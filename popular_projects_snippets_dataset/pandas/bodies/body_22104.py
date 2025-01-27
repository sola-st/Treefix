# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
result = self._op_via_apply(
    "hist",
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
    bins=bins,
    backend=backend,
    legend=legend,
    **kwargs,
)
exit(result)
