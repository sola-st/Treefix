# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/timeseries.py
data = getattr(ax, "_plot_data", None)

# clear current axes and data
ax._plot_data = []
ax.clear()

decorate_axes(ax, freq, kwargs)

lines = []
labels = []
if data is not None:
    for series, plotf, kwds in data:
        series = series.copy()
        idx = series.index.asfreq(freq, how="S")
        series.index = idx
        ax._plot_data.append((series, plotf, kwds))

        # for tsplot
        if isinstance(plotf, str):
            from pandas.plotting._matplotlib import PLOT_CLASSES

            plotf = PLOT_CLASSES[plotf]._plot

        lines.append(plotf(ax, series.index._mpl_repr(), series.values, **kwds)[0])
        labels.append(pprint_thing(series.name))

exit((lines, labels))
