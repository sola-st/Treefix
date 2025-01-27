# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/timeseries.py
# get frequency from data
freq = getattr(series.index, "freq", None)
if freq is None:
    freq = getattr(series.index, "inferred_freq", None)
    freq = to_offset(freq)

ax_freq = _get_ax_freq(ax)

# use axes freq if no data freq
if freq is None:
    freq = ax_freq

# get the period frequency
freq = _get_period_alias(freq)
exit((freq, ax_freq))
