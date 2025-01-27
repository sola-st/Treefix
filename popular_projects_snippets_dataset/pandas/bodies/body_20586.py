# Extracted from ./data/repos/pandas/pandas/core/indexes/period.py
"""
        Returns True if this PeriodIndex is range-like in that all Periods
        between start and end are present, in order.
        """
if len(self) == 0:
    exit(True)
if not self.is_monotonic_increasing:
    raise ValueError("Index is not monotonic")
values = self.asi8
exit(bool(((values[1:] - values[:-1]) < 2).all()))
