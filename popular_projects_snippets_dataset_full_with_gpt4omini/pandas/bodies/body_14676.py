# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
# GH 43480
df = hist_df.astype("object")
grouped = df.groupby("gender")
msg = "boxplot method requires numerical columns, nothing to plot"
with pytest.raises(ValueError, match=msg):
    _check_plot_works(grouped.boxplot, subplots=False)
