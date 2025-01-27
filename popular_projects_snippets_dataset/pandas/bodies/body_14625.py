# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# date
idx = [date(2000, 1, 1), date(2000, 1, 5), date(2000, 1, 20)]
df = DataFrame(np.random.randn(len(idx), 3), Index(idx, dtype=object))
_check_plot_works(df.plot)

# np.datetime64
idx = date_range("1/1/2000", periods=10)
idx = idx[[0, 2, 5, 9]].astype(object)
df = DataFrame(np.random.randn(len(idx), 3), idx)
_, ax = self.plt.subplots()
_check_plot_works(df.plot, ax=ax)
