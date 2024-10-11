# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimes.py
# adapted from _Timestamp._assert_tzawareness_compat
other_tz = getattr(other, "tzinfo", None)
other_dtype = getattr(other, "dtype", None)

if is_datetime64tz_dtype(other_dtype):
    # Get tzinfo from Series dtype
    other_tz = other.dtype.tz
if other is NaT:
    # pd.NaT quacks both aware and naive
    pass
elif self.tz is None:
    if other_tz is not None:
        raise TypeError(
            "Cannot compare tz-naive and tz-aware datetime-like objects."
        )
elif other_tz is None:
    raise TypeError(
        "Cannot compare tz-naive and tz-aware datetime-like objects"
    )
