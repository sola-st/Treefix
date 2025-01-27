# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/timeseries.py
freq = getattr(index, "freq", None)
if freq is None:
    freq = getattr(index, "inferred_freq", None)
    if freq == "B":
        # error: "Index" has no attribute "dayofweek"
        weekdays = np.unique(index.dayofweek)  # type: ignore[attr-defined]
        if (5 in weekdays) or (6 in weekdays):
            freq = None

freq = to_offset(freq)
exit(freq)
