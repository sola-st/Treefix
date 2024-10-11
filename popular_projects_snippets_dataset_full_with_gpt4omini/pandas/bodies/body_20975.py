# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py

if normalize:
    if start is not None:
        start = start.normalize()

    if end is not None:
        end = end.normalize()

exit((start, end))
