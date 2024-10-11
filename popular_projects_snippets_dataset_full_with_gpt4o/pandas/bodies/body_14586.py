# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
idx = date_range("2012-6-22 21:59:51", freq="S", periods=100)
df = DataFrame(np.random.randn(len(idx), 2), index=idx)

irreg = df.iloc[[0, 1, 3, 4]]
_, ax = self.plt.subplots()
irreg.plot(ax=ax)
diffs = Series(ax.get_lines()[0].get_xydata()[:, 0]).diff()

sec = 1.0 / 24 / 60 / 60
assert (np.fabs(diffs[1:] - [sec, sec * 2, sec]) < 1e-8).all()

_, ax = self.plt.subplots()
df2 = df.copy()
df2.index = df.index.astype(object)
df2.plot(ax=ax)
diffs = Series(ax.get_lines()[0].get_xydata()[:, 0]).diff()
assert (np.fabs(diffs[1:] - sec) < 1e-8).all()
