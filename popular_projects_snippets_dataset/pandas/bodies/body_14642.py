# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# test issue #8711
s = Series(range(5), timedelta_range("1day", periods=5))
_, ax = self.plt.subplots()
_check_plot_works(s.plot, ax=ax)

# test long period
index = timedelta_range("1 day 2 hr 30 min 10 s", periods=10, freq="1 d")
s = Series(np.random.randn(len(index)), index)
_, ax = self.plt.subplots()
_check_plot_works(s.plot, ax=ax)

# test short period
index = timedelta_range("1 day 2 hr 30 min 10 s", periods=10, freq="1 ns")
s = Series(np.random.randn(len(index)), index)
_, ax = self.plt.subplots()
_check_plot_works(s.plot, ax=ax)
