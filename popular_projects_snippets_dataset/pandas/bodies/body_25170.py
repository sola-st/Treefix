# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
x, y, data, C = self.x, self.y, self.data, self.C
ax = self.axes[0]
# pandas uses colormap, matplotlib uses cmap.
cmap = self.colormap or "BuGn"
cmap = mpl.colormaps.get_cmap(cmap)
cb = self.kwds.pop("colorbar", True)

if C is None:
    c_values = None
else:
    c_values = data[C].values

ax.hexbin(data[x].values, data[y].values, C=c_values, cmap=cmap, **self.kwds)
if cb:
    self._plot_colorbar(ax)
