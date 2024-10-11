# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
with tm.RNGContext(42):
    df = DataFrame(np.random.rand(6, 4), columns=["w", "x", "y", "z"])
    neg_df = -df
    # each column has either positive or negative value
    sep_df = DataFrame(
        {
            "w": np.random.rand(6),
            "x": np.random.rand(6),
            "y": -np.random.rand(6),
            "z": -np.random.rand(6),
        }
    )
    # each column has positive-negative mixed value
    mixed_df = DataFrame(
        np.random.randn(6, 4),
        index=list(string.ascii_letters[:6]),
        columns=["w", "x", "y", "z"],
    )

    ax1 = _check_plot_works(df.plot, kind=kind, stacked=False)
    ax2 = _check_plot_works(df.plot, kind=kind, stacked=True)
    self._compare_stacked_y_cood(ax1.lines, ax2.lines)

    ax1 = _check_plot_works(neg_df.plot, kind=kind, stacked=False)
    ax2 = _check_plot_works(neg_df.plot, kind=kind, stacked=True)
    self._compare_stacked_y_cood(ax1.lines, ax2.lines)

    ax1 = _check_plot_works(sep_df.plot, kind=kind, stacked=False)
    ax2 = _check_plot_works(sep_df.plot, kind=kind, stacked=True)
    self._compare_stacked_y_cood(ax1.lines[:2], ax2.lines[:2])
    self._compare_stacked_y_cood(ax1.lines[2:], ax2.lines[2:])

    _check_plot_works(mixed_df.plot, stacked=False)
    msg = (
        "When stacked is True, each column must be either all positive or "
        "all negative. Column 'w' contains both positive and negative "
        "values"
    )
    with pytest.raises(ValueError, match=msg):
        mixed_df.plot(stacked=True)

    # Use an index with strictly positive values, preventing
    #  matplotlib from warning about ignoring xlim
    df2 = df.set_index(df.index + 1)
    _check_plot_works(df2.plot, kind=kind, logx=True, stacked=True)
