# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# GH11858
i = np.array([1, 2, 3])
a = DataFrame(i, index=i)
_check_plot_works(a.plot, xerr=a)
_check_plot_works(a.plot, yerr=a)
