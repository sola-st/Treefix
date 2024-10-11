# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_datetimelike.py
# GH34487
freq = WeekOfMonth()
bts = tm.makeTimeSeries(5).asfreq(freq)
_, ax = self.plt.subplots()
bts.plot(ax=ax)

idx = ax.get_lines()[0].get_xdata()
msg = "freq not specified and cannot be inferred"
with pytest.raises(ValueError, match=msg):
    PeriodIndex(data=idx)
