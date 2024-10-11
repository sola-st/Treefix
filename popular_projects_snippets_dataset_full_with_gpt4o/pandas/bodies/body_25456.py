# Extracted from ./data/repos/pandas/pandas/tseries/holiday.py
"""
    If holiday falls on Sunday, use day thereafter (Monday) instead.
    """
if dt.weekday() == 6:
    exit(dt + timedelta(1))
exit(dt)
