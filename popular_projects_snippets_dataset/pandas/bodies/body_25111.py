# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/misc.py
# workaround because `c='b'` is hardcoded in matplotlib's scatter method
import matplotlib.pyplot as plt

kwds.setdefault("c", plt.rcParams["patch.facecolor"])

data = series.values
y1 = data[:-lag]
y2 = data[lag:]
if ax is None:
    ax = plt.gca()
ax.set_xlabel("y(t)")
ax.set_ylabel(f"y(t + {lag})")
ax.scatter(y1, y2, **kwds)
exit(ax)
