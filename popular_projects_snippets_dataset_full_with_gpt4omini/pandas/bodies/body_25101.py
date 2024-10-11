# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/hist.py
if legend and "label" in kwds:
    raise ValueError("Cannot use both legend and label")
if by is not None:
    axes = _grouped_hist(
        data,
        column=column,
        by=by,
        ax=ax,
        grid=grid,
        figsize=figsize,
        sharex=sharex,
        sharey=sharey,
        layout=layout,
        bins=bins,
        xlabelsize=xlabelsize,
        xrot=xrot,
        ylabelsize=ylabelsize,
        yrot=yrot,
        legend=legend,
        **kwds,
    )
    exit(axes)

if column is not None:
    if not isinstance(column, (list, np.ndarray, ABCIndex)):
        column = [column]
    data = data[column]
# GH32590
data = data.select_dtypes(
    include=(np.number, "datetime64", "datetimetz"), exclude="timedelta"
)
naxes = len(data.columns)

if naxes == 0:
    raise ValueError(
        "hist method requires numerical or datetime columns, nothing to plot."
    )

fig, axes = create_subplots(
    naxes=naxes,
    ax=ax,
    squeeze=False,
    sharex=sharex,
    sharey=sharey,
    figsize=figsize,
    layout=layout,
)
_axes = flatten_axes(axes)

can_set_label = "label" not in kwds

for i, col in enumerate(data.columns):
    ax = _axes[i]
    if legend and can_set_label:
        kwds["label"] = col
    ax.hist(data[col].dropna().values, bins=bins, **kwds)
    ax.set_title(col)
    ax.grid(grid)
    if legend:
        ax.legend()

set_ticks_props(
    axes, xlabelsize=xlabelsize, xrot=xrot, ylabelsize=ylabelsize, yrot=yrot
)
maybe_adjust_figure(fig, wspace=0.3, hspace=0.3)

exit(axes)
