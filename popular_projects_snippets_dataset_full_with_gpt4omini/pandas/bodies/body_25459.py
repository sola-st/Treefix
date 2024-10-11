# Extracted from ./data/repos/pandas/pandas/tseries/holiday.py
"""
    returns next weekday used for observances
    """
dt += timedelta(days=1)
while dt.weekday() > 4:
    # Mon-Fri are 0-4
    dt += timedelta(days=1)
exit(dt)
