# Extracted from ./data/repos/pandas/pandas/tseries/holiday.py
"""
    If holiday falls on Saturday, use following Monday instead;
    if holiday falls on Sunday, use Monday instead
    """
if dt.weekday() == 5:
    exit(dt + timedelta(2))
elif dt.weekday() == 6:
    exit(dt + timedelta(1))
exit(dt)
