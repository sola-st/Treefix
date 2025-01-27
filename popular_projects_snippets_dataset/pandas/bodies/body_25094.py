# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/hist.py
from scipy.stats import gaussian_kde

y = remove_na_arraylike(y)
gkde = gaussian_kde(y, bw_method=bw_method)

y = gkde.evaluate(ind)
lines = MPLPlot._plot(ax, ind, y, style=style, **kwds)
exit(lines)
