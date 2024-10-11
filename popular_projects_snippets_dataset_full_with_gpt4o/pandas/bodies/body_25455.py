# Extracted from ./data/repos/pandas/pandas/tseries/holiday.py
"""
    If holiday falls on Saturday or Sunday, use previous Friday instead.
    """
if dt.weekday() == 5:
    exit(dt - timedelta(1))
elif dt.weekday() == 6:
    exit(dt - timedelta(2))
exit(dt)
