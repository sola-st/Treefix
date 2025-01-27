# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# GH 3490 - irregular-timeseries with secondary y
from pandas.plotting._matplotlib.converter import DatetimeConverter

ts = tm.makeTimeSeries()[:20]
ts_irregular = ts[[1, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15, 17, 18]]

_, ax = self.plt.subplots()
ts_irregular[:5].plot(ax=ax)
# plot higher-x values on secondary axis
ts_irregular[5:].plot(secondary_y=True, ax=ax)
# ensure secondary limits aren't overwritten by plot on primary
ts_irregular[:5].plot(ax=ax)

left, right = ax.get_xlim()
assert left <= DatetimeConverter.convert(ts_irregular.index.min(), "", ax)
assert right >= DatetimeConverter.convert(ts_irregular.index.max(), "", ax)
