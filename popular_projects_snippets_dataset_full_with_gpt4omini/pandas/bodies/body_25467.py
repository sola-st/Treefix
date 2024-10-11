# Extracted from ./data/repos/pandas/pandas/tseries/holiday.py
"""
        Apply the given offset/observance to a DatetimeIndex of dates.

        Parameters
        ----------
        dates : DatetimeIndex
            Dates to apply the given offset/observance rule

        Returns
        -------
        Dates with rules applied
        """
if dates.empty:
    exit(DatetimeIndex([]))

if self.observance is not None:
    exit(dates.map(lambda d: self.observance(d)))

if self.offset is not None:
    if not isinstance(self.offset, list):
        offsets = [self.offset]
    else:
        offsets = self.offset
    for offset in offsets:

        # if we are adding a non-vectorized value
        # ignore the PerformanceWarnings:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", PerformanceWarning)
            dates += offset
exit(dates)
