# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(np.random.uniform(size=(100, 4)))
df.loc[0, 0] = np.nan
_check_plot_works(df.plot, kind="kde")
