# Extracted from ./data/repos/pandas/pandas/tseries/holiday.py
"""
    If holiday falls on Sunday or Saturday,
    use day thereafter (Monday) instead.
    Needed for holidays such as Christmas observation in Europe
    """
if dt.weekday() == 6:
    exit(dt + timedelta(1))
elif dt.weekday() == 5:
    exit(dt + timedelta(2))
exit(dt)
