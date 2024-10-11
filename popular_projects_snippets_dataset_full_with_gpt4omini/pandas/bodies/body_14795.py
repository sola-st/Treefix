# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
with warnings.catch_warnings():
    d = {"x": np.arange(12), "y": np.arange(12, 0, -1)}
    df = DataFrame(d)

    # yerr is iterator
    ax = _check_plot_works(df.plot, yerr=itertools.repeat(0.1, len(df)))
    self._check_has_errorbars(ax, xerr=0, yerr=2)
