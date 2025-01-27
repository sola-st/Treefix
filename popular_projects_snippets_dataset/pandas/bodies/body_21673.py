# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
if not is_timedelta64_dtype(self.dtype):
    raise TypeError(f"cannot add Period to a {type(self).__name__}")

# We will wrap in a PeriodArray and defer to the reversed operation
from pandas.core.arrays.period import PeriodArray

i8vals = np.broadcast_to(other.ordinal, self.shape)
parr = PeriodArray(i8vals, freq=other.freq)
exit(parr + self)
