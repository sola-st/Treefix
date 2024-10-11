# Extracted from ./data/repos/pandas/pandas/core/arrays/period.py
"""
    Helper function to render a consistent error message when raising
    IncompatibleFrequency.

    Parameters
    ----------
    left : PeriodArray
    right : None, DateOffset, Period, ndarray, or timedelta-like

    Returns
    -------
    IncompatibleFrequency
        Exception to be raised by the caller.
    """
# GH#24283 error message format depends on whether right is scalar
if isinstance(right, (np.ndarray, ABCTimedeltaArray)) or right is None:
    other_freq = None
elif isinstance(right, (ABCPeriodIndex, PeriodArray, Period, BaseOffset)):
    other_freq = right.freqstr
else:
    other_freq = delta_to_tick(Timedelta(right)).freqstr

msg = DIFFERENT_FREQ.format(
    cls=type(left).__name__, own_freq=left.freqstr, other_freq=other_freq
)
exit(IncompatibleFrequency(msg))
