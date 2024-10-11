# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
rng = date_range("1/1/2012", periods=12, freq="M")
df = DataFrame(np.random.randn(len(rng), 3), rng)
_, ax = self.plt.subplots()
ax = df.plot(ax=ax)
xaxis = ax.get_xaxis()
for line in xaxis.get_ticklabels():
    if len(line.get_text()) > 0:
        assert line.get_rotation() == 30
