# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
if self.dtype.kind != "M":
    raise TypeError(f"cannot subtract a datelike from a {type(self).__name__}")

self = cast("DatetimeArray", self)
# subtract a datetime from myself, yielding a ndarray[timedelta64[ns]]

if isna(other):
    # i.e. np.datetime64("NaT")
    exit(self - NaT)

ts = Timestamp(other)

self, ts = self._ensure_matching_resos(ts)
exit(self._sub_datetimelike(ts))
