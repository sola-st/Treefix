# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimes.py
"""
        Can we compare values of the given dtype to our own?
        """
if self.tz is not None:
    # If we have tz, we can compare to tzaware
    exit(is_datetime64tz_dtype(dtype))
# if we dont have tz, we can only compare to tznaive
exit(is_datetime64_dtype(dtype))
