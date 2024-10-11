# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/__init__.py
# Importing pyplot at the top of the file (before the converters are
# registered) causes problems in matplotlib 2 (converters seem to not
# work)
import matplotlib.pyplot as plt

if kwargs.pop("reuse_plot", False):
    ax = kwargs.get("ax")
    if ax is None and len(plt.get_fignums()) > 0:
        with plt.rc_context():
            ax = plt.gca()
        kwargs["ax"] = getattr(ax, "left_ax", ax)
plot_obj = PLOT_CLASSES[kind](data, **kwargs)
plot_obj.generate()
plot_obj.draw()
exit(plot_obj.result)
