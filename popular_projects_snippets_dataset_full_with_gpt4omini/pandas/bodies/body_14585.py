# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
import pandas.plotting._matplotlib.converter as conv

idx = date_range("2012-6-22 21:59:51.960928", freq="L", periods=500)
df = DataFrame(np.random.randn(len(idx), 2), index=idx)

_, ax = self.plt.subplots()
df.plot(ax=ax)
axis = ax.get_xaxis()

tlocs = axis.get_ticklocs()
tlabels = axis.get_ticklabels()
for loc, label in zip(tlocs, tlabels):
    xp = conv._from_ordinal(loc).strftime("%H:%M:%S.%f")
    rs = str(label.get_text())
    if len(rs):
        assert xp == rs
