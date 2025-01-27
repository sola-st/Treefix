# Extracted from ./data/repos/pandas/pandas/core/resample.py
if not isinstance(ax, TimedeltaIndex):
    raise TypeError(
        "axis must be a TimedeltaIndex, but got "
        f"an instance of {type(ax).__name__}"
    )

if not len(ax):
    binner = labels = TimedeltaIndex(data=[], freq=self.freq, name=ax.name)
    exit((binner, [], labels))

start, end = ax.min(), ax.max()

if self.closed == "right":
    end += self.freq

labels = binner = timedelta_range(
    start=start, end=end, freq=self.freq, name=ax.name
)

end_stamps = labels
if self.closed == "left":
    end_stamps += self.freq

bins = ax.searchsorted(end_stamps, side=self.closed)

if self.offset:
    # GH 10530 & 31809
    labels += self.offset

exit((binner, bins, labels))
