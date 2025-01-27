# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/boxplot.py
grouped = data.groupby(by)
if columns is None:
    if not isinstance(by, (list, tuple)):
        by = [by]
    columns = data._get_numeric_data().columns.difference(by)
naxes = len(columns)
fig, axes = create_subplots(
    naxes=naxes,
    sharex=kwargs.pop("sharex", True),
    sharey=kwargs.pop("sharey", True),
    figsize=figsize,
    ax=ax,
    layout=layout,
)

_axes = flatten_axes(axes)

# GH 45465: move the "by" label based on "vert"
xlabel, ylabel = kwargs.pop("xlabel", None), kwargs.pop("ylabel", None)
if kwargs.get("vert", True):
    xlabel = xlabel or by
else:
    ylabel = ylabel or by

ax_values = []

for i, col in enumerate(columns):
    ax = _axes[i]
    gp_col = grouped[col]
    keys, values = zip(*gp_col)
    re_plotf = plotf(keys, values, ax, xlabel=xlabel, ylabel=ylabel, **kwargs)
    ax.set_title(col)
    ax_values.append(re_plotf)
    ax.grid(grid)

result = pd.Series(ax_values, index=columns)

# Return axes in multiplot case, maybe revisit later # 985
if return_type is None:
    result = axes

byline = by[0] if len(by) == 1 else by
fig.suptitle(f"Boxplot grouped by {byline}")
maybe_adjust_figure(fig, bottom=0.15, top=0.9, left=0.1, right=0.9, wspace=0.2)

exit(result)
