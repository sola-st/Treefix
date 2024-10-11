# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/timeseries.py
"""Initialize axes for time-series plotting"""
if not hasattr(ax, "_plot_data"):
    ax._plot_data = []

ax.freq = freq
xaxis = ax.get_xaxis()
xaxis.freq = freq
if not hasattr(ax, "legendlabels"):
    ax.legendlabels = [kwargs.get("label", None)]
else:
    ax.legendlabels.append(kwargs.get("label", None))
ax.view_interval = None
ax.date_axis_info = None
