# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
d = {"x": np.arange(12), "y": np.arange(12, 0, -1)}
d_err = {"x": np.ones(12) * 0.2, "y": np.ones(12) * 0.4}

# check time-series plots
ix = date_range("1/1/2000", "1/1/2001", freq="M")
tdf = DataFrame(d, index=ix)
tdf_err = DataFrame(d_err, index=ix)

ax = _check_plot_works(tdf.plot, yerr=tdf_err, kind=kind)
self._check_has_errorbars(ax, xerr=0, yerr=2)

ax = _check_plot_works(tdf.plot, yerr=d_err, kind=kind)
self._check_has_errorbars(ax, xerr=0, yerr=2)

ax = _check_plot_works(tdf.plot, y="y", yerr=tdf_err["x"], kind=kind)
self._check_has_errorbars(ax, xerr=0, yerr=1)

ax = _check_plot_works(tdf.plot, y="y", yerr="x", kind=kind)
self._check_has_errorbars(ax, xerr=0, yerr=1)

ax = _check_plot_works(tdf.plot, yerr=tdf_err, kind=kind)
self._check_has_errorbars(ax, xerr=0, yerr=2)

axes = _check_plot_works(
    tdf.plot,
    default_axes=True,
    kind=kind,
    yerr=tdf_err,
    subplots=True,
)
self._check_has_errorbars(axes, xerr=0, yerr=1)
