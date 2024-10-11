# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_hist_box_by.py
# GH 15079
axes = _check_plot_works(
    hist_df.plot.hist, column=column, by=by, default_axes=True
)
result_titles = [ax.get_title() for ax in axes]
result_legends = [
    [legend.get_text() for legend in ax.get_legend().texts] for ax in axes
]

assert result_legends == legends
assert result_titles == titles
