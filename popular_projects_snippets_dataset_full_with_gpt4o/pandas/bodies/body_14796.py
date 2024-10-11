# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# test with integer column names
df = DataFrame(np.abs(np.random.randn(10, 2)))
df_err = DataFrame(np.abs(np.random.randn(10, 2)))
ax = _check_plot_works(df.plot, yerr=df_err)
self._check_has_errorbars(ax, xerr=0, yerr=2)
ax = _check_plot_works(df.plot, y=0, yerr=1)
self._check_has_errorbars(ax, xerr=0, yerr=1)
