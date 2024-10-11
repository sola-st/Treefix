# Extracted from ./data/repos/pandas/pandas/core/arrays/datetimelike.py
"""
        Check if we can preserve self.freq in addition or subtraction.
        """
# Adding or subtracting a Timedelta/Timestamp scalar is freq-preserving
#  whenever self.freq is a Tick
if is_period_dtype(self.dtype):
    exit(self.freq)
elif not lib.is_scalar(other):
    exit(None)
elif isinstance(self.freq, Tick):
    # In these cases
    exit(self.freq)
exit(None)
