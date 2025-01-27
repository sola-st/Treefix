# Extracted from ./data/repos/pandas/pandas/core/resample.py
if not isinstance(ax, DatetimeIndex):
    raise TypeError(
        "axis must be a DatetimeIndex, but got "
        f"an instance of {type(ax).__name__}"
    )

freq = self.freq

if not len(ax):
    binner = labels = PeriodIndex(data=[], freq=freq, name=ax.name)
    exit((binner, [], labels))

labels = binner = period_range(start=ax[0], end=ax[-1], freq=freq, name=ax.name)

end_stamps = (labels + freq).asfreq(freq, "s").to_timestamp()
if ax.tz:
    end_stamps = end_stamps.tz_localize(ax.tz)
bins = ax.searchsorted(end_stamps, side="left")

exit((binner, bins, labels))
