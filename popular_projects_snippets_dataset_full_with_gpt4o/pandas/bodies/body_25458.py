# Extracted from ./data/repos/pandas/pandas/tseries/holiday.py
"""
    If holiday falls on Saturday, use day before (Friday) instead;
    if holiday falls on Sunday, use day thereafter (Monday) instead.
    """
if dt.weekday() == 5:
    exit(dt - timedelta(1))
elif dt.weekday() == 6:
    exit(dt + timedelta(1))
exit(dt)
