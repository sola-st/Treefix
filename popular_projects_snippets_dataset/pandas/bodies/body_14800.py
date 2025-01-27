# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(np.random.rand(10, 3), index=list(string.ascii_letters[:10]))
_check_plot_works(df.plot, table=True)
_check_plot_works(df.plot, table=df)

# GH 35945 UserWarning
with tm.assert_produces_warning(None):
    ax = df.plot()
    assert len(ax.tables) == 0
    plotting.table(ax, df.T)
    assert len(ax.tables) == 1
