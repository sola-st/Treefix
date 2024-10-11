# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
if not is_timedelta64_dtype(self.dtype):
    raise TypeError(
        f"cannot add {type(self).__name__} and {type(other).__name__}"
    )

# defer to DatetimeArray.__add__
exit(other + self)
