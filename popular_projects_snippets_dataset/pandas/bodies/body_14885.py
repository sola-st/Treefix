# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
expected = np.array([1e-1, 1e0, 1e1, 1e2, 1e3, 1e4])

_, ax = self.plt.subplots()
ax = Series([200, 500]).plot.bar(log=True, ax=ax)
tm.assert_numpy_array_equal(ax.yaxis.get_ticklocs(), expected)
tm.close()

_, ax = self.plt.subplots()
ax = Series([200, 500]).plot.barh(log=True, ax=ax)
tm.assert_numpy_array_equal(ax.xaxis.get_ticklocs(), expected)
tm.close()

# GH 9905
expected = np.array([1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1e0, 1e1])

_, ax = self.plt.subplots()
ax = Series([0.1, 0.01, 0.001]).plot(log=True, kind="bar", ax=ax)
ymin = 0.0007943282347242822
ymax = 0.12589254117941673
res = ax.get_ylim()
tm.assert_almost_equal(res[0], ymin)
tm.assert_almost_equal(res[1], ymax)
tm.assert_numpy_array_equal(ax.yaxis.get_ticklocs(), expected)
tm.close()

_, ax = self.plt.subplots()
ax = Series([0.1, 0.01, 0.001]).plot(log=True, kind="barh", ax=ax)
res = ax.get_xlim()
tm.assert_almost_equal(res[0], ymin)
tm.assert_almost_equal(res[1], ymax)
tm.assert_numpy_array_equal(ax.xaxis.get_ticklocs(), expected)
