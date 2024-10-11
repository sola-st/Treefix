# Extracted from ./data/repos/pandas/pandas/core/resample.py
if not isinstance(ax, DatetimeIndex):
    raise TypeError(
        "axis must be a DatetimeIndex, but got "
        f"an instance of {type(ax).__name__}"
    )

if len(ax) == 0:
    binner = labels = DatetimeIndex(data=[], freq=self.freq, name=ax.name)
    exit((binner, [], labels))

first, last = _get_timestamp_range_edges(
    ax.min(),
    ax.max(),
    self.freq,
    closed=self.closed,
    origin=self.origin,
    offset=self.offset,
)
# GH #12037
# use first/last directly instead of call replace() on them
# because replace() will swallow the nanosecond part
# thus last bin maybe slightly before the end if the end contains
# nanosecond part and lead to `Values falls after last bin` error
# GH 25758: If DST lands at midnight (e.g. 'America/Havana'), user feedback
# has noted that ambiguous=True provides the most sensible result
binner = labels = date_range(
    freq=self.freq,
    start=first,
    end=last,
    tz=ax.tz,
    name=ax.name,
    ambiguous=True,
    nonexistent="shift_forward",
).as_unit(ax.unit)

ax_values = ax.asi8
binner, bin_edges = self._adjust_bin_edges(binner, ax_values)

# general version, knowing nothing about relative frequencies
bins = lib.generate_bins_dt64(
    ax_values, bin_edges, self.closed, hasnans=ax.hasnans
)

if self.closed == "right":
    labels = binner
    if self.label == "right":
        labels = labels[1:]
elif self.label == "right":
    labels = labels[1:]

if ax.hasnans:
    binner = binner.insert(0, NaT)
    labels = labels.insert(0, NaT)

# if we end up with more labels than bins
# adjust the labels
# GH4076
if len(bins) < len(labels):
    labels = labels[: len(bins)]

exit((binner, bins, labels))
