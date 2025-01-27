# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# https://github.com/matplotlib/matplotlib/issues/8459
rng = date_range("1/1/2011", periods=10, freq="H")
x = rng
w1 = np.arange(0, 1, 0.1)
w2 = np.arange(0, 1, 0.1)[::-1]
_, ax = self.plt.subplots()
ax.hist([x, x], weights=[w1, w2])
