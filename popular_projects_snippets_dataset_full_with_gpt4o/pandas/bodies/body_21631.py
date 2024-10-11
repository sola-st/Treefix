# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
# used for Timedelta/DatetimeArray, overwritten by PeriodArray
if is_object_dtype(dtype):
    exit(np.array(list(self), dtype=object))
exit(self._ndarray)
