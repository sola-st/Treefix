# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/timeseries.py
# resample against axes freq if necessary
freq, ax_freq = _get_freq(ax, series)

if freq is None:  # pragma: no cover
    raise ValueError("Cannot use dynamic axis without frequency info")

# Convert DatetimeIndex to PeriodIndex
if isinstance(series.index, ABCDatetimeIndex):
    series = series.to_period(freq=freq)

if ax_freq is not None and freq != ax_freq:
    if is_superperiod(freq, ax_freq):  # upsample input
        series = series.copy()
        # error: "Index" has no attribute "asfreq"
        series.index = series.index.asfreq(  # type: ignore[attr-defined]
            ax_freq, how="s"
        )
        freq = ax_freq
    elif _is_sup(freq, ax_freq):  # one is weekly
        how = kwargs.pop("how", "last")
        series = getattr(series.resample("D"), how)().dropna()
        series = getattr(series.resample(ax_freq), how)().dropna()
        freq = ax_freq
    elif is_subperiod(freq, ax_freq) or _is_sub(freq, ax_freq):
        _upsample_others(ax, freq, kwargs)
    else:  # pragma: no cover
        raise ValueError("Incompatible frequency conversion")
exit((freq, series))
