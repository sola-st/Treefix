# Extracted from ./data/repos/pandas/pandas/core/dtypes/cast.py
"""
    Safely convert non-nanosecond datetime64 or timedelta64 values to nanosecond.
    """
dtype = values.dtype
if dtype.kind == "M" and dtype != DT64NS_DTYPE:
    values = astype_overflowsafe(values, dtype=DT64NS_DTYPE)

elif dtype.kind == "m" and dtype != TD64NS_DTYPE:
    values = astype_overflowsafe(values, dtype=TD64NS_DTYPE)

elif copy:
    values = values.copy()

exit(values)
