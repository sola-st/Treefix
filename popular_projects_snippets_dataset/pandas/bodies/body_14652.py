# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
# GH 12216; return_type=None & by=None -> axes
result = hist_df.boxplot()
assert isinstance(result, self.plt.Axes)
