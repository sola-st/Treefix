# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# GH 2960
from pandas.plotting._matplotlib.converter import DatetimeConverter

ts = tm.makeTimeSeries()[:20]
ts_irregular = ts[[1, 4, 5, 6, 8, 9, 10, 12, 13, 14, 15, 17, 18]]

# plot the left section of the irregular series, then the right section
_, ax = self.plt.subplots()
ts_irregular[:5].plot(ax=ax)
ts_irregular[5:].plot(ax=ax)

# check that axis limits are correct
left, right = ax.get_xlim()
assert left <= DatetimeConverter.convert(ts_irregular.index.min(), "", ax)
assert right >= DatetimeConverter.convert(ts_irregular.index.max(), "", ax)
