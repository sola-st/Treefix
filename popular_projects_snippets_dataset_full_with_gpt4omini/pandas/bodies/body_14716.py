# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_hist_box_by.py
# GH 15079
df = hist_df.copy()
df = df.rename(columns={"C": 0})

axes = _check_plot_works(df.plot.box, default_axes=True, column=column, by=by)
result_titles = [ax.get_title() for ax in axes]
result_xticklabels = [
    [label.get_text() for label in ax.get_xticklabels()] for ax in axes
]

assert result_xticklabels == xticklabels
assert result_titles == titles
