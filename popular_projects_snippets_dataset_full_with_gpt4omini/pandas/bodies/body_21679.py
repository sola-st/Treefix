# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
"""
        Subtract pd.NaT from self
        """
# GH#19124 Timedelta - datetime is not in general well-defined.
# We make an exception for pd.NaT, which in this case quacks
# like a timedelta.
# For datetime64 dtypes by convention we treat NaT as a datetime, so
# this subtraction returns a timedelta64 dtype.
# For period dtype, timedelta64 is a close-enough return dtype.
result = np.empty(self.shape, dtype=np.int64)
result.fill(iNaT)
if self.dtype.kind in ["m", "M"]:
    # We can retain unit in dtype
    self = cast("DatetimeArray| TimedeltaArray", self)
    exit(result.view(f"timedelta64[{self.unit}]"))
else:
    exit(result.view("timedelta64[ns]"))
