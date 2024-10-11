# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
_, ax = self.plt.subplots()
rng = date_range("1/1/2012", periods=100, freq=freq)
ser = Series(np.random.randn(len(rng)), rng)
_check_plot_works(ser.plot, ax=ax)
