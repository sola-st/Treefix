# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_hist_method.py
_check_plot_works(ts.hist)
_check_plot_works(ts.hist, grid=False)
_check_plot_works(ts.hist, figsize=(8, 10))
# _check_plot_works adds an ax so catch warning. see GH #13188
with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    _check_plot_works(ts.hist, by=ts.index.month)
with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
    _check_plot_works(ts.hist, by=ts.index.month, bins=5)

fig, ax = self.plt.subplots(1, 1)
_check_plot_works(ts.hist, ax=ax, default_axes=True)
_check_plot_works(ts.hist, ax=ax, figure=fig, default_axes=True)
_check_plot_works(ts.hist, figure=fig, default_axes=True)
tm.close()

fig, (ax1, ax2) = self.plt.subplots(1, 2)
_check_plot_works(ts.hist, figure=fig, ax=ax1, default_axes=True)
_check_plot_works(ts.hist, figure=fig, ax=ax2, default_axes=True)

msg = (
    "Cannot pass 'figure' when using the 'by' argument, since a new 'Figure' "
    "instance will be created"
)
with pytest.raises(ValueError, match=msg):
    ts.hist(by=ts.index, figure=fig)
