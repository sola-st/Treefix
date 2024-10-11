# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
s = Series(range(10), dtype=object)
_check_plot_works(s.plot, kind=kind)
