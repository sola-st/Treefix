# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/timeseries.py
# tsplot converts automatically, but don't want to convert index
# over and over for DataFrames
if isinstance(data.index, (ABCDatetimeIndex, ABCPeriodIndex)):
    freq: str | BaseOffset | None = data.index.freq

    if freq is None:
        # We only get here for DatetimeIndex
        data.index = cast("DatetimeIndex", data.index)
        freq = data.index.inferred_freq
        freq = to_offset(freq)

    if freq is None:
        freq = _get_ax_freq(ax)

    if freq is None:
        raise ValueError("Could not get frequency alias for plotting")

    freq_str = _get_period_alias(freq)

    if isinstance(data.index, ABCDatetimeIndex):
        data = data.tz_localize(None).to_period(freq=freq_str)
    elif isinstance(data.index, ABCPeriodIndex):
        data.index = data.index.asfreq(freq=freq_str)
exit(data)
