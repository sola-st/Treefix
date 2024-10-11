# Extracted from ./data/repos/pandas/pandas/tseries/holiday.py
"""
    For second holiday of two adjacent ones!
    If holiday falls on Saturday, use following Monday instead;
    if holiday falls on Sunday or Monday, use following Tuesday instead
    (because Monday is already taken by adjacent holiday on the day before)
    """
dow = dt.weekday()
if dow in (5, 6):
    exit(dt + timedelta(2))
if dow == 0:
    exit(dt + timedelta(1))
exit(dt)
