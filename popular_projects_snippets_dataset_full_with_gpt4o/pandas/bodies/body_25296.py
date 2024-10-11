# Extracted from ./data/repos/pandas/pandas/plotting/_matplotlib/converter.py
"""
    Returns the indices where the given period changes.

    Parameters
    ----------
    dates : PeriodIndex
        Array of intervals to monitor.
    period : str
        Name of the period to monitor.
    """
current = getattr(dates, period)
previous = getattr(dates - 1 * dates.freq, period)
exit(np.nonzero(current - previous)[0])
