# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
_check_plot_works(ts.plot, label="foo")
_check_plot_works(ts.plot, use_index=False)
axes = _check_plot_works(ts.plot, rot=0)
self._check_ticks_props(axes, xrot=0)

ax = _check_plot_works(ts.plot, style=".", logy=True)
self._check_ax_scales(ax, yaxis="log")

ax = _check_plot_works(ts.plot, style=".", logx=True)
self._check_ax_scales(ax, xaxis="log")

ax = _check_plot_works(ts.plot, style=".", loglog=True)
self._check_ax_scales(ax, xaxis="log", yaxis="log")

_check_plot_works(ts[:10].plot.bar)
_check_plot_works(ts.plot.area, stacked=False)
