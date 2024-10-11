# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
result = self._op_via_apply(
    "hist",
    by=by,
    ax=ax,
    grid=grid,
    xlabelsize=xlabelsize,
    xrot=xrot,
    ylabelsize=ylabelsize,
    yrot=yrot,
    figsize=figsize,
    bins=bins,
    backend=backend,
    legend=legend,
    **kwargs,
)
exit(result)
