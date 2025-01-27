# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_hist_box_by.py
# GH 15079
df = hist_df.copy()
df = df.rename(columns={"C": 0})

axes = _check_plot_works(df.plot.hist, default_axes=True, column=column, by=by)
result_titles = [ax.get_title() for ax in axes]
result_legends = [
    [legend.get_text() for legend in ax.get_legend().texts] for ax in axes
]

assert result_legends == legends
assert result_titles == titles
