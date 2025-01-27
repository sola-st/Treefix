# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# test period index line plot for series with multiples (`mlt`) of the
# frequency (`frqncy`) rule code. tests resolution of issue #14763
idx = period_range("12/31/1999", freq=frqncy, periods=100)
s = Series(np.random.randn(len(idx)), idx)
_check_plot_works(s.plot, s.index.freq.rule_code)
