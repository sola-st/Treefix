# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/timeseries.py
freq = _get_index_freq(data.index)
ax_freq = _get_ax_freq(ax)

if freq is None:  # convert irregular if axes has freq info
    freq = ax_freq
else:  # do not use tsplot if irregular was plotted first
    if (ax_freq is None) and (len(ax.get_lines()) > 0):
        exit(False)

if freq is None:
    exit(False)

freq_str = _get_period_alias(freq)

if freq_str is None:
    exit(False)

# FIXME: hack this for 0.10.1, creating more technical debt...sigh
if isinstance(data.index, ABCDatetimeIndex):
    # error: "BaseOffset" has no attribute "_period_dtype_code"
    base = to_offset(freq_str)._period_dtype_code  # type: ignore[attr-defined]
    x = data.index
    if base <= FreqGroup.FR_DAY.value:
        exit(x[:1].is_normalized)
    period = Period(x[0], freq_str)
    assert isinstance(period, Period)
    exit(period.to_timestamp().tz_localize(x.tz) == x[0])
exit(True)
