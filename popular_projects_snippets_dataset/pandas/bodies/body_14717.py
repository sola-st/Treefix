# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_hist_box_by.py
# GH 15079
msg = "No group keys passed"
with pytest.raises(ValueError, match=msg):
    _check_plot_works(hist_df.plot.box, default_axes=True, column=column, by=by)
