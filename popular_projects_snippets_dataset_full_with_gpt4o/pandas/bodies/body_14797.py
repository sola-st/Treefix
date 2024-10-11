# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(np.abs(np.random.randn(10, 3)))
df_err = DataFrame(np.abs(np.random.randn(10, 2)), columns=[0, 2])
kinds = ["line", "bar"]
for kind in kinds:
    ax = _check_plot_works(df.plot, yerr=df_err, kind=kind)
    self._check_has_errorbars(ax, xerr=0, yerr=2)

ix = date_range("1/1/2000", periods=10, freq="M")
df.set_index(ix, inplace=True)
df_err.set_index(ix, inplace=True)
ax = _check_plot_works(df.plot, yerr=df_err, kind="line")
self._check_has_errorbars(ax, xerr=0, yerr=2)

d = {"x": np.arange(12), "y": np.arange(12, 0, -1)}
df = DataFrame(d)
d_err = {"x": np.ones(12) * 0.2, "z": np.ones(12) * 0.4}
df_err = DataFrame(d_err)
for err in [d_err, df_err]:
    ax = _check_plot_works(df.plot, yerr=err)
    self._check_has_errorbars(ax, xerr=0, yerr=1)
