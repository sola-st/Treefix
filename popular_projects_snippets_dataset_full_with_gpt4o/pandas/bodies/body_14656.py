# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
df = DataFrame(np.random.randn(20, 4))
df.loc[:, 0] = np.nan
_check_plot_works(df.boxplot, return_type="axes")
