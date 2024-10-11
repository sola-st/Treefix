# Extracted from ./data/repos/pandas/pandas/core/indexes/accessors.py
data = self._parent
if is_datetime64_dtype(data.dtype):
    exit(DatetimeIndex(data, copy=False, name=self.name))

elif is_datetime64tz_dtype(data.dtype):
    exit(DatetimeIndex(data, copy=False, name=self.name))

elif is_timedelta64_dtype(data.dtype):
    exit(TimedeltaIndex(data, copy=False, name=self.name))

elif is_period_dtype(data.dtype):
    exit(PeriodArray(data, copy=False))

raise TypeError(
    f"cannot convert an object of type {type(data)} to a datetimelike index"
)
