# Extracted from ./data/repos/pandas/pandas/core/arrays/period.py
# We handle Period[T] -> Period[U]
# Our parent handles everything else.
dtype = pandas_dtype(dtype)
if is_dtype_equal(dtype, self._dtype):
    if not copy:
        exit(self)
    else:
        exit(self.copy())
if is_period_dtype(dtype):
    exit(self.asfreq(dtype.freq))

if is_datetime64_any_dtype(dtype):
    # GH#45038 match PeriodIndex behavior.
    tz = getattr(dtype, "tz", None)
    exit(self.to_timestamp().tz_localize(tz))

exit(super().astype(dtype, copy=copy))
