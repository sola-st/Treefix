# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
d = {"x": np.arange(12), "y": np.arange(12, 0, -1)}
df = DataFrame(d)
d_err = {"x": np.ones(12) * 0.2, "y": np.ones(12) * 0.4}
df_err = DataFrame(d_err)

ax = _check_plot_works(df.plot, yerr=df_err["x"], kind=kind)
self._check_has_errorbars(ax, xerr=0, yerr=2)

ax = _check_plot_works(df.plot, yerr=d_err, kind=kind)
self._check_has_errorbars(ax, xerr=0, yerr=2)

ax = _check_plot_works(df.plot, yerr=df_err, xerr=df_err, kind=kind)
self._check_has_errorbars(ax, xerr=2, yerr=2)

ax = _check_plot_works(df.plot, yerr=df_err["x"], xerr=df_err["x"], kind=kind)
self._check_has_errorbars(ax, xerr=2, yerr=2)

ax = _check_plot_works(df.plot, xerr=0.2, yerr=0.2, kind=kind)
self._check_has_errorbars(ax, xerr=2, yerr=2)

axes = _check_plot_works(
    df.plot,
    default_axes=True,
    yerr=df_err,
    xerr=df_err,
    subplots=True,
    kind=kind,
)
self._check_has_errorbars(axes, xerr=1, yerr=1)
