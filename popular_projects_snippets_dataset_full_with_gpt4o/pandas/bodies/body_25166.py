# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
x, y, c, data = self.x, self.y, self.c, self.data
ax = self.axes[0]

c_is_column = is_hashable(c) and c in self.data.columns

color_by_categorical = c_is_column and is_categorical_dtype(self.data[c])

color = self.kwds.pop("color", None)
if c is not None and color is not None:
    raise TypeError("Specify exactly one of `c` and `color`")
if c is None and color is None:
    c_values = self.plt.rcParams["patch.facecolor"]
elif color is not None:
    c_values = color
elif color_by_categorical:
    c_values = self.data[c].cat.codes
elif c_is_column:
    c_values = self.data[c].values
else:
    c_values = c

if self.colormap is not None:
    cmap = mpl.colormaps.get_cmap(self.colormap)
else:
    # cmap is only used if c_values are integers, otherwise UserWarning
    if is_integer_dtype(c_values):
        # pandas uses colormap, matplotlib uses cmap.
        cmap = "Greys"
        cmap = mpl.colormaps[cmap]
    else:
        cmap = None

if color_by_categorical:
    from matplotlib import colors

    n_cats = len(self.data[c].cat.categories)
    cmap = colors.ListedColormap([cmap(i) for i in range(cmap.N)])
    bounds = np.linspace(0, n_cats, n_cats + 1)
    norm = colors.BoundaryNorm(bounds, cmap.N)
else:
    norm = self.kwds.pop("norm", None)
# plot colorbar if
# 1. colormap is assigned, and
# 2.`c` is a column containing only numeric values
plot_colorbar = self.colormap or c_is_column
cb = self.kwds.pop("colorbar", is_numeric_dtype(c_values) and plot_colorbar)

if self.legend and hasattr(self, "label"):
    label = self.label
else:
    label = None
scatter = ax.scatter(
    data[x].values,
    data[y].values,
    c=c_values,
    label=label,
    cmap=cmap,
    norm=norm,
    **self.kwds,
)
if cb:
    cbar_label = c if c_is_column else ""
    cbar = self._plot_colorbar(ax, label=cbar_label)
    if color_by_categorical:
        cbar.set_ticks(np.linspace(0.5, n_cats - 0.5, n_cats))
        cbar.ax.set_yticklabels(self.data[c].cat.categories)

if label is not None:
    self._append_legend_handles_labels(scatter, label)
else:
    self.legend = False

errors_x = self._get_errorbars(label=x, index=0, yerr=False)
errors_y = self._get_errorbars(label=y, index=0, xerr=False)
if len(errors_x) > 0 or len(errors_y) > 0:
    err_kwds = dict(errors_x, **errors_y)
    err_kwds["ecolor"] = scatter.get_facecolor()[0]
    ax.errorbar(data[x].values, data[y].values, linestyle="none", **err_kwds)
