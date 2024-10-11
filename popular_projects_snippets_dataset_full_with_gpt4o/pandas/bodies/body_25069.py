# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/timeseries.py
legend = ax.get_legend()
lines, labels = _replot_ax(ax, freq, kwargs)
_replot_ax(ax, freq, kwargs)

other_ax = None
if hasattr(ax, "left_ax"):
    other_ax = ax.left_ax
if hasattr(ax, "right_ax"):
    other_ax = ax.right_ax

if other_ax is not None:
    rlines, rlabels = _replot_ax(other_ax, freq, kwargs)
    lines.extend(rlines)
    labels.extend(rlabels)

if legend is not None and kwargs.get("legend", True) and len(lines) > 0:
    title = legend.get_title().get_text()
    if title == "None":
        title = None
    ax.legend(lines, labels, loc="best", title=title)
