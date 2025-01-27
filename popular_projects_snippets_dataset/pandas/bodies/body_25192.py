# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/core.py
LinePlot._post_plot_logic(self, ax, data)

is_shared_y = len(list(ax.get_shared_y_axes())) > 0
# do not override the default axis behaviour in case of shared y axes
if self.ylim is None and not is_shared_y:
    if (data >= 0).all().all():
        ax.set_ylim(0, None)
    elif (data <= 0).all().all():
        ax.set_ylim(None, 0)
