# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
import matplotlib as mpl

def_colors = self._unpack_cycler(mpl.rcParams)
index = date_range("1/1/2000", periods=12)
s = Series(np.arange(1, 13), index=index)

ncolors = 3

_, ax = self.plt.subplots()
for i in range(ncolors):
    ax = s.plot(ax=ax)
self._check_colors(ax.get_lines(), linecolors=def_colors[:ncolors])
