# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
s = Series(np.random.uniform(size=50))
s[0] = np.nan
axes = _check_plot_works(s.plot.kde)

# gh-14821: check if the values have any missing values
assert any(~np.isnan(axes.lines[0].get_xdata()))
