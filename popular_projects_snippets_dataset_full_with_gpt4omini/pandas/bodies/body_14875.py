# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
# GH 6951
ax = _check_plot_works(ts.plot, subplots=True)
self._check_axes_shape(ax, axes_num=1, layout=(1, 1))

ax = _check_plot_works(ts.plot, subplots=True, layout=(-1, 1))
self._check_axes_shape(ax, axes_num=1, layout=(1, 1))
ax = _check_plot_works(ts.plot, subplots=True, layout=(1, -1))
self._check_axes_shape(ax, axes_num=1, layout=(1, 1))
