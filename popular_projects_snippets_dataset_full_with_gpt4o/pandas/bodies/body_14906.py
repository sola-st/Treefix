# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py

s = Series(np.arange(10), name="x")
s_err = np.abs(np.random.randn(10))
d_err = DataFrame(
    np.abs(np.random.randn(10, 2)), index=s.index, columns=["x", "y"]
)
# test line and bar plots
kinds = ["line", "bar"]
for kind in kinds:
    ax = _check_plot_works(s.plot, yerr=Series(s_err), kind=kind)
    self._check_has_errorbars(ax, xerr=0, yerr=1)
    ax = _check_plot_works(s.plot, yerr=s_err, kind=kind)
    self._check_has_errorbars(ax, xerr=0, yerr=1)
    ax = _check_plot_works(s.plot, yerr=s_err.tolist(), kind=kind)
    self._check_has_errorbars(ax, xerr=0, yerr=1)
    ax = _check_plot_works(s.plot, yerr=d_err, kind=kind)
    self._check_has_errorbars(ax, xerr=0, yerr=1)
    ax = _check_plot_works(s.plot, xerr=0.2, yerr=0.2, kind=kind)
    self._check_has_errorbars(ax, xerr=1, yerr=1)

ax = _check_plot_works(s.plot, xerr=s_err)
self._check_has_errorbars(ax, xerr=1, yerr=0)

# test time series plotting
ix = date_range("1/1/2000", "1/1/2001", freq="M")
ts = Series(np.arange(12), index=ix, name="x")
ts_err = Series(np.abs(np.random.randn(12)), index=ix)
td_err = DataFrame(np.abs(np.random.randn(12, 2)), index=ix, columns=["x", "y"])

ax = _check_plot_works(ts.plot, yerr=ts_err)
self._check_has_errorbars(ax, xerr=0, yerr=1)
ax = _check_plot_works(ts.plot, yerr=td_err)
self._check_has_errorbars(ax, xerr=0, yerr=1)

# check incorrect lengths and types
with tm.external_error_raised(ValueError):
    s.plot(yerr=np.arange(11))

s_err = ["zzz"] * 10
with tm.external_error_raised(TypeError):
    s.plot(yerr=s_err)
