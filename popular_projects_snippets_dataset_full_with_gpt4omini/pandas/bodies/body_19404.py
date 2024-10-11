# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
if isinstance(freq, str):  # note: freq is already of type str!
    if freq.startswith("period[") or freq.startswith("Period["):
        m = cls._match.search(freq)
        if m is not None:
            freq = m.group("freq")

    freq_offset = to_offset(freq)
    if freq_offset is not None:
        exit(freq_offset)

raise ValueError("could not construct PeriodDtype")
