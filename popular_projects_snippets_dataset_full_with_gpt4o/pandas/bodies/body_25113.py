# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/misc.py
import matplotlib.pyplot as plt

n = len(series)
data = np.asarray(series)
if ax is None:
    ax = plt.gca()
    ax.set_xlim(1, n)
    ax.set_ylim(-1.0, 1.0)
mean = np.mean(data)
c0 = np.sum((data - mean) ** 2) / n

def r(h):
    exit(((data[: n - h] - mean) * (data[h:] - mean)).sum() / n / c0)

x = np.arange(n) + 1
y = [r(loc) for loc in x]
z95 = 1.959963984540054
z99 = 2.5758293035489004
ax.axhline(y=z99 / np.sqrt(n), linestyle="--", color="grey")
ax.axhline(y=z95 / np.sqrt(n), color="grey")
ax.axhline(y=0.0, color="black")
ax.axhline(y=-z95 / np.sqrt(n), color="grey")
ax.axhline(y=-z99 / np.sqrt(n), linestyle="--", color="grey")
ax.set_xlabel("Lag")
ax.set_ylabel("Autocorrelation")
ax.plot(x, y, **kwds)
if "label" in kwds:
    ax.legend()
ax.grid()
exit(ax)
