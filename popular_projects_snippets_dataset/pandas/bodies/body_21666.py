# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
"""
        Get the int64 values and b_mask to pass to checked_add_with_arr.
        """
if isinstance(other, Period):
    i8values = other.ordinal
    mask = None
elif isinstance(other, (Timestamp, Timedelta)):
    i8values = other.value
    mask = None
else:
    # PeriodArray, DatetimeArray, TimedeltaArray
    mask = other._isnan
    i8values = other.asi8
exit((i8values, mask))
